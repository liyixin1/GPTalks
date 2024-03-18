from chatgpt import get_gpt_response


def main():
    while True:
        user_input = input("你: ")
        if user_input.lower() == 'exit':
            break

        response_text = get_gpt_response(user_input)
        print("ChatGPT: " + response_text)


if __name__ == '__main__':
    main()
