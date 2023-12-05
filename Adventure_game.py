import random

class AdventureGameNode:
    def __init__(self, story_text, options=None):
        self.story_text = story_text
        self.options = options or {}

    def add_option(self, option_number, option_text, next_node):
        self.options[str(option_number)] = (option_text, next_node)

def play_adventure_game(current_node):
    if callable(current_node):
        current_node()
        return

    print(current_node.story_text)
    if not current_node.options:
        end_game()
        return

    print("선택지:")
    for option_number, option in current_node.options.items():
        option_text = option[0]
        print(f"{option_number}. {option_text}")

    selected_option = input("선택하세요: ")
    if selected_option in current_node.options:
        next_node = current_node.options[selected_option][1]
        play_adventure_game(next_node)
    else:
        print("유효한 선택지가 아닙니다. 다시 선택해주세요.")

def treasure_hunt_game(route):
    print("보물 찾기 미니게임을 시작합니다!")
    target_number = random.randint(1, 100)
    is_game_over = False

    while not is_game_over:
        user_guess = input("1부터 100 사이의 숫자를 추측해보세요: ")

        try:
            user_guess = int(user_guess)
            if user_guess < 1 or user_guess > 100:
                print("숫자는 1부터 100 사이로 입력해주세요.")
            elif user_guess == target_number:
                print("축하합니다! 보물을 찾았습니다!")
                is_game_over = True
                if route == "forest":
                    sad_ending()
                elif route == "sea":
                    happy_ending()
            elif user_guess < target_number:
                print("숫자가 작습니다. 다시 시도해보세요.")
            else:
                print("숫자가 큽니다. 다시 시도해보세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

def happy_ending():
    print("당신은 보물에 도달하여 행복한 결말을 맞이했습니다. Happy Ending!")

def sad_ending():
    print("이 보물은 사실 빈 보물상자였습니다. Sad Ending...")

def end_game():
    print("게임이 종료되었습니다. 이용해주셔서 감사합니다!")

# 게임 노드 생성
start_node = AdventureGameNode("잃어버린 보물의 비밀에 대한 이야기가 전해지고 있습니다.\n당신은 보물사냥꾼입니다. 보물을 찾기 위해 가는 중입니다.")

node2_1 = AdventureGameNode("숲 속으로 들어왔습니다. 숲 속 안에 다른 모험가와 얘기하다 보물 위치에 대한 단서를 얻게되었습니다.")
node2_1_1 = AdventureGameNode("오두막 안에 들어갔습니다. 오두막 안 산적이 당신을 죽였습니다.")
node3_1 = AdventureGameNode("벙커 안에 들어갔습니다. 벙커 안 쪽 보물을 발견했지만 가는 길에 함정이 설치되어 있는 것 같습니다.")
node3_1_1 = AdventureGameNode("당신은 함정에 걸려 죽었습니다.")
node4_1 = AdventureGameNode("당신은 보물에 도달하여 최종 보물에 도착하였습니다. 비밀번호를 맞추기 위해 미니게임을 시작합니다.")

node2_2 = AdventureGameNode("바다에 도착했습니다. 바다 근처 동굴에 보물이 있다는 단서를 발견하게 되는데,")
node2_2_1 = AdventureGameNode("당신의 배의 폭탄이 있어서 터져서 죽었습니다.")
node3_2 = AdventureGameNode("당신은 동굴 안에 도착하였습니다.\n동굴 안 쪽에 보물을 발견했지만 가는 길에 함정이 설치되어 있는 것 같습니다.")
node3_2_1 = AdventureGameNode("당신은 함정에 걸려 찔려 죽었습니다.")
node4_2 = AdventureGameNode("당신은 보물에 도달하여 최종 보물에 도착하였습니다. 비밀번호를 맞추기 위해 미니게임을 시작합니다.")


# 선택지 추가
start_node.add_option(1, "숲으로 향합니다.", node2_1)
start_node.add_option(2, "바다로 향합니다.", node2_2)

node2_1.add_option(1, "큰 나무 위에 있는 오두막 집에 들어갑니다.", node2_1_1)
node2_1.add_option(2, "땅 밑 벙커를 발견하여 들어갑니다.", node3_1)
node3_1.add_option(1, "보물까지 기어간다.", node4_1)
node3_1.add_option(2, "보물까지 뛰어간다.", node3_1_1)
node4_1.add_option(1, "미니게임을 시작합니다!", lambda: treasure_hunt_game("forest"))

node2_2.add_option(1, "돛단배를 타고 간다.", node2_2_1)
node2_2.add_option(2, "잠수 장비를 입고 간다.", node3_2)
node3_2.add_option(1, "기어간다.", node4_2)
node3_2.add_option(2, "뛰어간다.", node3_2_1)
node4_2.add_option(1, "미니게임을 시작합니다!", lambda: treasure_hunt_game("sea"))


# 게임 시작
print("잃어버린 보물의 비밀에 대한 여행을 시작합니다!")
play_adventure_game(start_node)
