from pathlib import Path

import cv2
import numpy as np

from hats.registry.hat_tags import HatTagRegistry

SCREENSHOTS_DIR = Path("media/test")
SLOT_BG_COLOR = np.array([139, 139, 139])
NUM_SLOT_BG_PIXELS = 80 * 80 + 2 * 5 * 5


def extract_slots_from_screenshot(
    screenshot, start: tuple[int, int], num_slots: tuple[int, int], slot_size_pixels: int
):
    for y in map(lambda x: start[1] + x * slot_size_pixels, range(num_slots[1])):
        for x in map(lambda x: start[0] + x * slot_size_pixels, range(num_slots[0])):
            yield screenshot[y : y + slot_size_pixels, x : x + slot_size_pixels]


def num_pixels_of_color(img, color: np.ndarray):
    mask = cv2.inRange(img, color, color)
    output = cv2.bitwise_and(img, img, mask=mask)
    return np.count_nonzero(output) / color.size


def get_nonempty_slots_from_screenshot(screenshot):
    slots = extract_slots_from_screenshot(
        screenshot, start=(875, 240), num_slots=(9, 6), slot_size_pixels=90
    )
    return filter(lambda s: num_pixels_of_color(s, SLOT_BG_COLOR) != NUM_SLOT_BG_PIXELS, slots)


def main():
    registry = HatTagRegistry.get()

    for path in SCREENSHOTS_DIR.iterdir():
        hat_types = registry[path.stem]

        slots = get_nonempty_slots_from_screenshot(cv2.imread(str(path)))
        for slot, hat_type in zip(slots, hat_types):
            cv2.imshow(hat_type, slot)
            cv2.waitKey(0)


main()
