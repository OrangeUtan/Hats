import itertools
from pathlib import Path

import cv2
import numpy as np

from hats.registry.hat_tags import HatTagRegistry

SCREENSHOTS_DIR = Path("media/test")


def extract_slots_from_screenshot(
    screenshot, start: tuple[int, int], num_slots: tuple[int, int], slot_size: int, slot_margin: int
):
    for x in map(lambda x: start[0] + x * slot_size, range(num_slots[0])):
        for y in map(lambda x: start[1] + x * slot_size, range(num_slots[1])):
            yield screenshot[
                y + slot_margin : y + slot_size - slot_margin,
                x + slot_margin : x + slot_size - slot_margin,
            ]


def num_pixels_of_color(img, color: np.ndarray):
    mask = cv2.inRange(img, color, color)
    output = cv2.bitwise_and(img, img, mask=mask)
    return int(np.count_nonzero(output) / color.size)


def get_nonempty_slots_from_screenshot(screenshot, slot_size: int, slot_margin: int, slot_bg_color):
    num_slot_bg_pixels = (slot_size - 2 * slot_margin) ** 2

    inventory_slots = extract_slots_from_screenshot(
        screenshot, start=(830, 635), num_slots=(9, 3), slot_size=slot_size, slot_margin=slot_margin
    )
    hotbar_slots = extract_slots_from_screenshot(
        screenshot, start=(830, 925), num_slots=(9, 1), slot_size=slot_size, slot_margin=slot_margin
    )
    slots = itertools.chain(hotbar_slots, inventory_slots)

    return filter(lambda s: num_pixels_of_color(s, slot_bg_color) != num_slot_bg_pixels, slots)


def increase_hsv(img, hue, satturation, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - hue
    h[h > lim] = 255
    h[h <= lim] += hue

    lim = 255 - satturation
    s[s > lim] = 255
    s[s <= lim] += satturation

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)
    return img


def main():
    registry = HatTagRegistry.get()
    bg_color = np.array([250, 250, 250, 255])

    for path in SCREENSHOTS_DIR.iterdir():
        hat_types = registry[path.stem]

        screenshot = cv2.imread(str(path))
        if screenshot is None:
            continue
        screenshot = cv2.addWeighted(screenshot, 1.8, screenshot, 0, 0)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2RGBA)

        slots = get_nonempty_slots_from_screenshot(screenshot, 90, 5, bg_color)
        for slot, hat_type in zip(slots, hat_types):
            mask = cv2.inRange(slot, bg_color, bg_color)
            slot[mask > 0] = (0, 0, 0, 0)
            print(hat_type)
            cv2.imwrite(f"media/test/slots/{hat_type}.jpg", slot)


main()
