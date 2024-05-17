def calculate_load(mass, gravity=9.81):
    return mass * gravity


def calculate_stress(load, area):
    return load / area


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")


def main():
    while True:
        print("LS계산기")
        print("1. 하중 계산")
        print("2. 응력 계산")
        print("3. 종료")

        choice = input("선택 (1,2,3): ")

        if choice == '1':
            mass = get_positive_float("질량(kg)을 입력하세요: ")
            load = calculate_load(mass)
            print(f"계산된 하중은 {load:.2f} N 입니다.")

        elif choice == '2':
            load = get_positive_float("하중(N)을 입력하세요: ")
            area = get_positive_float("단면적(m^2)을 입력하세요: ")
            stress = calculate_stress(load, area)
            print(f"계산된 응력은 {stress:.2f} Pa 입니다.")

        elif choice == '3':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()