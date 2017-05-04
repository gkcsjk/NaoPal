import csv
import os


# Headers of csv file
fieldnames = ["RShoulderRoll", "LShoulderRoll", "RShoulderPitch", "LShoulderPitch",
              "RElbowRoll", "LElbowRoll", "RElbowYaw", "LElbowYaw", "HeadYaw", "HeadPitch",
              "RWristYaw", "LWristYaw"]

# fieldnames = ["RAnkleRoll", "LAnkleRoll", "RAnklePitch", "LAnklePitch", "RKneePitch",
#               "LKneePitch", "RHipRoll", "LHipRoll", "RHipPitch", "LHipPitch", "RHipYawPitch", "LHipYawPitch"]


def save_result(results, path):
    """
    Append the results at the end of the existing CSV file.
    """
    try:
        with open(path, "ab") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for result in results:
                writer.writerow(result)
    except Exception:
        return False
    else:
        return True


def create_csv(path, filename):
    """
    Create a new CSV file with the headers listed above.
    """
    path = os.path.join(path, filename).replace("\\", "/")
    with open(path, 'wb+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    print path
    return path


def load_result(path):
    """
    Load results from CSV file.
    """
    results = {}
    results["RShoulderRoll"] = []
    results["LShoulderRoll"] = []
    results["RShoulderPitch"] = []
    results["LShoulderPitch"] = []
    results["RElbowRoll"] = []
    results["LElbowRoll"] = []
    results["RElbowYaw"] = []
    results["LElbowYaw"] = []
    results["HeadYaw"] = []
    results["HeadPitch"] = []
    results["RWristYaw"] = []
    results["LWristYaw"] = []
    results["HeadYaw"] = []
    results["HeadPitch"] = []
    results["RWristYaw"] = []
    results["LWristYaw"] = []
    # results["RAnkleRoll"] = []
    # results["LAnkleRoll"] = []
    # results["RAnklePitch"] = []
    # results["LAnklePitch"] = []
    # results["RKneePitch"] = []
    # results["LKneePitch"] = []
    # results["RHipRoll"] = []
    # results["LHipRoll"] = []
    # results["RHipPitch"] = []
    # results["LHipPitch"] = []
    # results["RHipYawPitch"] = []
    # results["LHipYawPitch"] = []

    with open(path, "rb") as csvfile:
        reader = csv.DictReader(csvfile)
        length = 0
        for row in reader:
            length += 1
            for fieldname in fieldnames:
                results[fieldname].append(float(row[fieldname]))
    return results, length

