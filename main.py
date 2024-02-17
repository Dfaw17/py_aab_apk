import subprocess
import sys
import os
import multiprocessing
import time

sys.path.append(f"{os.path.abspath(os.getcwd())}")

use_OS = "WINDOWS"


def task1():
    subprocess.call(
        ["java", "-jar", "bundletool-all-1.15.6.jar", "build-apks", "--bundle=extract_apk/universal.aab",
         "--output=extract_apk/universal.apks", "--mode=universal"])


def task2():
    if use_OS == "MAC":
        subprocess.call(["unzip", "extract_apk/universal.apks", "-d", "extract_apk/"])

    if use_OS == "WINDOWS":
        os.rename("extract_apk/universal.apks", "extract_apk/universal.zip")
        time.sleep(3)
        subprocess.call(["tar", "-xf", "extract_apk/universal.zip", "-C", "extract_apk"])


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    p1.start()
    time.sleep(10)
    p2.start()

    p1.join()
    p2.join()
