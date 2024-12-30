class FileHandler:
    def copy_file(self, input_file, output_file):
        try:
            with open(input_file, 'r') as file:
                content = file.read()

            with open(output_file, 'w') as file:
                file.write(content)

            print(f"Content copied from '{input_file}' to '{output_file}'.")
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the input file path: ").strip()
    output_file = input("Enter the output file path: ").strip()

    fileHandler = FileHandler()
    
    fileHandler.copy_file(input_file, output_file)
