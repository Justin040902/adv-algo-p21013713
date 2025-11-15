class Person:
    def __init__(self, name: str, gender: str, biography: str = "", privacy: str = "public"):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy  # "public" or "private"

    def __str__(self) -> str:
        """String representation for display"""
        if self.privacy == "private":
            return f"Name: {self.name}\nPrivacy: Private profile - details hidden"
        else:
            return f"Name: {self.name}\nGender: {self.gender}\nBio: {self.biography}\nPrivacy: {self.privacy}"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def get_public_info(self) -> str:
        """Get only public information"""
        return f"Name: {self.name}\nPrivacy: {self.privacy}"


