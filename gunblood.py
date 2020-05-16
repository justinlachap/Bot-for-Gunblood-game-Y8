import pyautogui
import time

# MAXIMISE SCREEN AT https://fr.y8.com/games/gunblood
# Remove adblock

reloadX, reloadY = 475, 910
enemyheadX, enemyheadY = 1417, 465
enemybodyX, enemybodyY = 1319, 680
nextRoundX, nextRoundY = 975, 767


def reload():
    pyautogui.moveTo(reloadX, reloadY)


def shoot():
    pyautogui.moveTo(enemyheadX, enemyheadY)
    for i in range(2):
        pyautogui.click()
    pyautogui.moveTo(enemybodyX, enemybodyY)
    for j in range(5):
        pyautogui.click()


def next_level():
    pyautogui.moveTo(nextRoundX, nextRoundY)
    pyautogui.click()


rounds = 0
bonusRounds = [3, 6, 9, 12]

if __name__ == '__main__':
    while True:
        rounds += 1
        if rounds in bonusRounds:
            time.sleep(0.3)
            pyautogui.moveTo(963, 648)  # coordinate for bonus round
            pyautogui.click()
            shoot()
            time.sleep(2)
            next_level()
            time.sleep(0.2)
        else:
            reload()
            time.sleep(1.8)
            shoot()
            time.sleep(1.5)
            next_level()
            time.sleep(0.2)
