from mcanitexgen import Sequence, State, TextureAnimation, animation


@animation("head.png")
class Head(TextureAnimation):
    NEUTRAL = State(0)
    TILTED = State(1)
    DOWN = State(2)
    BLINK = State(3)
    MOUTH_OPEN = State(4)
    ONE_EYE = State(5)

    blink = Sequence(BLINK(duration=4))

    peek = Sequence(ONE_EYE(duration=25))

    panting = Sequence(MOUTH_OPEN(weight=1), DOWN(duration=5))

    panting_n_blinking = Sequence(2 * panting(weight=1), blink)

    blinking = Sequence(DOWN(weight=1), blink)

    bored = Sequence(7 * blinking(duration=120))

    fall_asleep = Sequence(DOWN(duration=50), peek)

    asleep = Sequence(
        BLINK(weight=1),
        peek(mark="peek_while_sleeping"),
        BLINK(weight=1),
    )

    wake_up = Sequence(peek, DOWN(duration=50))

    happy = Sequence(4 * panting_n_blinking(duration=150))

    curious = Sequence(
        NEUTRAL(weight=1),
        TILTED(weight=1),
        NEUTRAL(weight=1),
        TILTED(weight=15),
    )

    main = Sequence(
        bored,
        fall_asleep,
        asleep(duration=600, mark="asleep"),
        wake_up,
        happy,
        curious(duration=400),
        NEUTRAL(duration=20),
    )


@animation("tail_and_hindlegs.png")
class TailAndHindlegs(TextureAnimation):
    TAIL_HIGH = State(0)
    TAIL_NEUTRAL = State(1)
    TAIL_LOW = State(2)
    LEG_LEFT_HIGH = State(3)
    LEG_RIGHT_HIGH = State(4)

    kick_legs = Sequence(LEG_LEFT_HIGH(duration=12), LEG_RIGHT_HIGH(duration=12))

    bored = Sequence(5 * kick_legs, TAIL_LOW(duration=80))

    wag_tail = Sequence(TAIL_NEUTRAL(weight=1), TAIL_HIGH(weight=1))

    varied_wagging = Sequence(9 * wag_tail(duration=10), 4 * wag_tail(duration=15))

    wagging_with_pause = Sequence(
        varied_wagging,
        TAIL_NEUTRAL(duration=10),
        TAIL_LOW(duration=40),
    )

    main = Sequence(
        4 * bored,
        TAIL_LOW(duration=790),
        3 * wagging_with_pause,
        TAIL_LOW(end=Head.end),
    )


@animation("dream.png")
class Dream(TextureAnimation):
    NONE = State(0)
    APPEAR1 = State(1)
    APPEAR2 = State(2)
    EMPTY_BUBBLE = State(3)
    STEAK_GROUND = State(4)
    STEAK_JUMPING = State(5)
    POP1 = State(6)
    POP2 = State(7)

    appear = Sequence(APPEAR1(weight=1), APPEAR2(weight=1), EMPTY_BUBBLE(weight=1))

    jumping_steak = Sequence(STEAK_GROUND(weight=1), STEAK_JUMPING(weight=1))

    pop = Sequence(POP1(weight=1), POP2(weight=1))

    main = Sequence(
        NONE(end=Head.marks["asleep"].start + 175),
        appear(duration=45),
        6 * jumping_steak(duration=10),
        STEAK_GROUND(duration=5),
        STEAK_JUMPING,
        pop(start=Head.marks["peek_while_sleeping"].start, duration=4),
        NONE(end=Head.end),
    )
