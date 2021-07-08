import logging
import re
from typing import Optional

from semantic_release.errors import UnknownCommitMessageStyleError
from semantic_release.helpers import LoggedFunction
from semantic_release.history.parser_helpers import ParsedCommit, parse_paragraphs, re_breaking

logger = logging.getLogger(__name__)


class ReleaseType:
    def __init__(self, commit_prefix: str, level_bump: int, type: Optional[str] = None):
        self.commit_prefix = commit_prefix
        self.level_bump = level_bump
        self.type = type or self.commit_prefix


# Supported commit types for parsing
TYPES_BY_PREFIX = {
    r.commit_prefix: r
    for r in [
        ReleaseType("ci", 0),
        ReleaseType("chore", 0),
        ReleaseType("refactor", 0),
        ReleaseType("fix", 1),
        ReleaseType("perf", 1, "performance"),
        ReleaseType("feat", 2, "feature"),
        ReleaseType("hat", 2),
    ]
}

re_parser = re.compile(
    r"(?P<prefix>" + "|".join(TYPES_BY_PREFIX.keys()) + ")"
    r"(?:\((?P<scope>[^\n]+)\))?"
    r"(?P<break>!)?: "
    r"(?P<subject>[^\n]+)"
    r"(:?\n\n(?P<text>.+))?",
    re.DOTALL,
)


@LoggedFunction(logger)
def parse_commit_message(message: str) -> ParsedCommit:

    # Attempt to parse the commit message with a regular expression
    parsed = re_parser.match(message)
    if not parsed:
        raise UnknownCommitMessageStyleError(f"Unable to parse the given commit message: {message}")

    descriptions: list[str] = [parsed.group("subject")]
    descriptions += parse_paragraphs(parsed.group("text")) if parsed.group("text") else list()

    # Look for descriptions of breaking changes
    breaking_descriptions = [
        match.group(1) for match in (re_breaking.match(p) for p in descriptions[1:]) if match
    ]

    if parsed.group("break") or breaking_descriptions:
        level_bump = 3  # Major
    else:
        level_bump = TYPES_BY_PREFIX[parsed.group("prefix")].level_bump

    return ParsedCommit(
        level_bump,
        TYPES_BY_PREFIX[parsed.group("prefix")].type,
        parsed.group("scope"),
        descriptions,
        breaking_descriptions,
    )
