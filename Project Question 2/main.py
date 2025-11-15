from graph import Graph
from person import Person


class SocialMediaApp:
    def __init__(self):
        self.social_graph = Graph[Person]()
        self.initialize_sample_data()

    def initialize_sample_data(self):
        """Initialize with sample person profiles"""
        # Create sample person profiles
        people = [
            Person("Alice Johnson", "Female", "Photography enthusiast and traveler", "public"),
            Person("Bob Smith", "Male", "Software developer and gamer", "public"),
            Person("Carol Davis", "Female", "Private account", "private"),
            Person("David Wilson", "Male", "Fitness coach and nutritionist", "public"),
            Person("Eva Brown", "Female", "Artist and designer", "public"),
            Person("Frank Miller", "Male", "Music producer", "private"),
            Person("Grace Lee", "Female", "Book lover and writer", "public"),
            Person("Henry Taylor", "Male", "Chef and food blogger", "public")
        ]

        # Add people to graph
        for person in people:
            self.social_graph.add_vertex(person)

        # Create follow relationships
        relationships = [
            (people[0], people[1]),  # Alice follows Bob
            (people[0], people[3]),  # Alice follows David
            (people[1], people[0]),  # Bob follows Alice
            (people[1], people[2]),  # Bob follows Carol
            (people[2], people[4]),  # Carol follows Eva
            (people[3], people[0]),  # David follows Alice
            (people[3], people[4]),  # David follows Eva
            (people[4], people[1]),  # Eva follows Bob
            (people[4], people[5]),  # Eva follows Frank
            (people[5], people[6]),  # Frank follows Grace
            (people[6], people[3]),  # Grace follows David
            (people[6], people[7]),  # Grace follows Henry
            (people[7], people[4]),  # Henry follows Eva
            (people[7], people[6]),  # Henry follows Grace
        ]

        for from_person, to_person in relationships:
            self.social_graph.add_edge(from_person, to_person)

    def display_all_users(self):
        """Display a list of all users' names"""
        print("\n" + "=" * 50)
        print("ALL USERS")
        print("=" * 50)
        for i, person in enumerate(self.social_graph.get_all_vertices(), 1):
            print(f"{i}. {person.name}")
        print("=" * 50)

    def view_profile_detail(self):
        """View the profile of any one person in detail"""
        self.display_all_users()
        try:
            choice = int(input("\nEnter the number of the person to view: ")) - 1
            people = self.social_graph.get_all_vertices()
            if 0 <= choice < len(people):
                person = people[choice]
                print("\n" + "=" * 50)
                print("PROFILE DETAILS")
                print("=" * 50)
                print(person)
                print("=" * 50)
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")

    def view_followed_accounts(self):
        """View the list of followed accounts of a particular person"""
        self.display_all_users()
        try:
            choice = int(input("\nEnter the number of the person: ")) - 1
            people = self.social_graph.get_all_vertices()
            if 0 <= choice < len(people):
                person = people[choice]
                followed = self.social_graph.list_outgoing_adjacent_vertex(person)

                print(f"\n{person.name} is following {len(followed)} people:")
                print("-" * 30)
                for i, followed_person in enumerate(followed, 1):
                    print(f"{i}. {followed_person.name}")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")

    def view_followers(self):
        """View the list of followers of a particular person"""
        self.display_all_users()
        try:
            choice = int(input("\nEnter the number of the person: ")) - 1
            people = self.social_graph.get_all_vertices()
            if 0 <= choice < len(people):
                person = people[choice]
                followers = self.social_graph.list_incoming_adjacent_vertex(person)

                print(f"\n{person.name} has {len(followers)} followers:")
                print("-" * 30)
                for i, follower in enumerate(followers, 1):
                    print(f"{i}. {follower.name}")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")

    def add_user_profile(self):
        """Add a new user profile on-demand"""
        print("\n" + "=" * 50)
        print("ADD NEW USER PROFILE")
        print("=" * 50)

        name = input("Enter name: ")
        gender = input("Enter gender: ")
        bio = input("Enter biography: ")
        privacy = input("Enter privacy (public/private): ").lower()

        if privacy not in ["public", "private"]:
            privacy = "public"

        new_person = Person(name, gender, bio, privacy)
        self.social_graph.add_vertex(new_person)
        print(f"\n✅ User '{name}' added successfully!")

    def follow_user(self):
        """Allow a user to follow another user on-demand"""
        self.display_all_users()
        try:
            follower_choice = int(input("\nEnter the number of the follower: ")) - 1
            followed_choice = int(input("Enter the number of the person to follow: ")) - 1

            people = self.social_graph.get_all_vertices()
            if (0 <= follower_choice < len(people) and
                    0 <= followed_choice < len(people)):

                follower = people[follower_choice]
                followed = people[followed_choice]

                if follower == followed:
                    print("You cannot follow yourself!")
                elif followed in self.social_graph.list_outgoing_adjacent_vertex(follower):
                    print(f"{follower.name} is already following {followed.name}!")
                else:
                    self.social_graph.add_edge(follower, followed)
                    print(f"✅ {follower.name} is now following {followed.name}!")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter valid numbers!")

    def unfollow_user(self):
        """Allow a user to unfollow another user on-demand"""
        self.display_all_users()
        try:
            follower_choice = int(input("\nEnter the number of the follower: ")) - 1
            people = self.social_graph.get_all_vertices()

            if 0 <= follower_choice < len(people):
                follower = people[follower_choice]
                followed_list = self.social_graph.list_outgoing_adjacent_vertex(follower)

                if not followed_list:
                    print(f"{follower.name} is not following anyone!")
                    return

                print(f"\n{follower.name} is following:")
                for i, person in enumerate(followed_list, 1):
                    print(f"{i}. {person.name}")

                unfollow_choice = int(input("\nEnter the number to unfollow: ")) - 1
                if 0 <= unfollow_choice < len(followed_list):
                    unfollowed = followed_list[unfollow_choice]
                    self.social_graph.remove_edge(follower, unfollowed)
                    print(f"✅ {follower.name} has unfollowed {unfollowed.name}!")
                else:
                    print("Invalid selection!")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter valid numbers!")

    def display_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 50)
        print("SOCIAL MEDIA APP")
        print("=" * 50)
        print("1. Display all users")
        print("2. View profile details")
        print("3. View followed accounts")
        print("4. View followers")
        print("5. Add new user profile")
        print("6. Follow user")
        print("7. Unfollow user")
        print("8. Exit")
        print("=" * 50)

    def run(self):
        """Run the main program loop"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                self.display_all_users()
            elif choice == '2':
                self.view_profile_detail()
            elif choice == '3':
                self.view_followed_accounts()
            elif choice == '4':
                self.view_followers()
            elif choice == '5':
                self.add_user_profile()
            elif choice == '6':
                self.follow_user()
            elif choice == '7':
                self.unfollow_user()
            elif choice == '8':
                print("Thank you for using Social Media App! Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = SocialMediaApp()
    app.run()
