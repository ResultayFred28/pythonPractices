import random
import string


TEST_MODE = True

# ---- values used only when TEST_MODE is True ----
membership_plan_test = "VIP"
item_variable_test = "access_token"
security_code_test = 5

# ============================================================
# LEVEL 1 - AGE & SCORE GATE
# ============================================================
age = int(input("enter your age: "))
score = int(input("enter your score: "))

print("=" * 50)
print("LEVEL 1: AGE & SCORE GATE")
print("=" * 50)
print("AGE:", age)
print("SCORE:", score)

age_score_ok = age >= 18 and score >= 50

if age_score_ok:
    print("ACCESS GRANTED!")
    print("Welcome to Cyber Arcade.")

    # ========================================================
    # LEVEL 2 - MEMBERSHIP SCANNER
    # ========================================================
    print()
    print("=" * 50)
    print("LEVEL 2: MEMBERSHIP SCANNER")
    print("=" * 50)

    if TEST_MODE:
        membership_plan = membership_plan_test
    else:
        # ---- instructor-provided random membership generator ----
        plans = ["VIP", "Regular", "Premium"]
        if random.choice([True, False]):
            membership_plan = random.choice(plans)
        else:
            membership_plan = ''.join(random.choices(string.ascii_letters, k=6))
        # -----------------------------------------------------------

    print("MEMBERSHIP:", membership_plan)

    if membership_plan == "VIP":
        print("ACCESS GRANTED!")
        print("VIP access granted.")
    elif membership_plan == "Premium":
        print("ACCESS GRANTED!")
        print("Premium access granted.")
    elif membership_plan == "Regular":
        print("ACCESS GRANTED!")
        print("Regular access only.")
    else:
        print("ACCESS DENIED!")
        print("Invalid Membership.")

    # A membership only lets the player continue if it was one of the
    # three recognized tiers. Written with `or` so we do not need a
    # list/tuple of valid plans just to test membership.
    membership_valid = (membership_plan == "VIP") or \
                       (membership_plan == "Premium") or \
                       (membership_plan == "Regular")

    if membership_valid:

        # ====================================================
        # LEVEL 3 - INVENTORY CHECK
        # ====================================================
        print()
        print("=" * 50)
        print("LEVEL 3: INVENTORY CHECK")
        print("=" * 50)

        if TEST_MODE:
            item_variable = item_variable_test
        else:
            # ---- instructor-provided random item generator ----
            items = ["keycard", "badge", "access_token", "coin", "ticket", "flashlight"]
            item_variable = random.choice(items)
            # -------------------------------------------------------

        print("Item:", item_variable)

        # Membership (`in`) check instead of comparing item_variable to
        # every accepted value one by one. Commas pad both sides so
        # "token" can never falsely match inside "access_token".
        accepted_items = ", keycard, badge, access_token,"
        item_wrapped = ", " + item_variable + ","
        item_valid = item_wrapped in accepted_items

        if item_valid:
            print("Valid Items Provided!")
            print("Proceed to the next checkpoint.")
        else:
            print("Invalid Items Provided")
            print("Do not proceed.")

        if item_valid:

            # ================================================
            # LEVEL 4 - SECURITY FLAG CHALLENGE
            # ================================================
            print()
            print("=" * 50)
            print("LEVEL 4: SECURITY FLAG CHALLENGE")
            print("=" * 50)

            if TEST_MODE:
                security_code = security_code_test
            else:
                # ---- instructor-provided random code generator ----
                security_code = random.randint(1, 20)
                # -------------------------------------------------------

            code_bitconversion = bin(security_code)
            print("Security Code:", security_code)
            print("Binary Code:", code_bitconversion)

            # Bit 0 (value 1) = PLAYER flag, bit 1 (value 2) = ADMIN flag.
            # '&' compares matching bits: the result is 0 only when the
            # arcade's flag bit and the security code's bit are not both 1.
            player_flag = security_code & 1
            admin_flag = security_code & 2

            if player_flag != 0:
                player_status = "On"
            else:
                player_status = "Off"

            if admin_flag != 0:
                admin_status = "On"
            else:
                admin_status = "Off"

            print("Player:", player_status)
            print("Admin:", admin_status)

            if player_flag != 0 and admin_flag != 0:
                print("Player and Admin Access Provided!")
            elif player_flag != 0 and admin_flag == 0:
                print("Player Access Provided!")
            elif player_flag == 0 and admin_flag != 0:
                print("Admin Access Provided!")
            else:
                print("Guest Access Provided")

            # ================================================
            # LEVEL 5 - VIP CHALLENGE ROOM
            # ================================================
            print()
            print("=" * 50)
            print("LEVEL 5: VIP CHALLENGE ROOM")
            print("=" * 50)

            # "Basic requirements": still old/skilled enough (Level 1)
            # and still carrying a valid item (Level 3).
            basic_requirements_ok = age_score_ok and item_valid

            if basic_requirements_ok:

                # "VIP requirements": VIP membership AND the security
                # code must carry the PLAYER flag but NOT the ADMIN flag
                # ("Security Code is Player only").
                vip_requirements_ok = (membership_plan == "VIP") and \
                                      (player_flag != 0 and admin_flag == 0)

                if vip_requirements_ok:
                    print("ACCESS GRANTED!")
                    print("Welcome to the VIP Challenge Room.")
                else:
                    print("ACCESS DENIED!")
                    print("VIP requirements not met.")
            else:
                print("ACCESS DENIED!")
                print("Arcade access requirements not met.")

        else:
            print()
            print("Program stopped: invalid item at Level 3.")

    else:
        print()
        print("Program stopped: invalid membership at Level 2.")

else:
    print("ACCESS DENIED!")
    print("Age Restriction.")
    print()
    print("Program stopped: requirements not met at Level 1.")
