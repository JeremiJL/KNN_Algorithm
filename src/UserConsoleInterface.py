from Classifier import *
from ClassifierPlus import *

# Greet user
print("Welcome to my KNN Algorithm Implementation!\n")

# Ask user for data necessary to build classifier
train_file_path = input("Please provide train data file path : ")
k_value = int(input("Please provide value for K : "))

# Create classifier object
classifier = Classifier(train_file_path, k_value)

# Loop condition
running = True

# User interface loop
while running:
    user_input = input("\nWhat would you like to now?\n"
                       "a) Evaluate model accuracy\n"
                       "b) Classify given observation\n"
                       "c) Quit\n"
                       "d) Draw bar plot of accuracy as a function of K\n"
                       "Option : ")

    if user_input == 'a':
        # Ask user for path of test data file and form of output
        test_file_path = input("Please provide test data file path : ")
        share_each_result = input("Do you want to see detailed info about the result of every sample test?"
                                  "\n[Yes / No] : ")
        # Print result of accuracy evaluation
        print("Accuracy of the model is:",
              classifier.evaluate_accuracy(test_file_path, share_each_result.title() == 'Yes'))

    elif user_input == 'b':
        # Inform user about input format
        print("Please provide " + str(classifier.num_of_attributes) + " attributes values, one at a time.")
        # Ask user for attribute value, one at a time
        attributes = []
        for attribute in range(0, classifier.num_of_attributes):
            attributes.append(float(input("Provide attribute value : ")))
        # After collecting all values, classify observation
        result = classifier.classify(Observation(label="", attributes_values=attributes))
        # Print result
        print("Result of classification : " + result)

    elif user_input == 'c':
        print("Bye bye!")
        running = False

    elif user_input == 'd':
        # Ask user for path of test data file and form of output
        test_file_path = input("Please provide test data file path : ")
        # Ask user up to what number of k model should perform computations
        max_k = input("Up to what number of k, should the model evaluate accuracy?\n"
                      "Provide value of k : ")
        ClassifierPlus(classifier.train_file_path, classifier.k_val).plot_accuracy_as_a_function_of_k(test_file_path, int(max_k))
        print("To view the image, close the program.")

    else:
        print("Invalid option. Please try again.")
