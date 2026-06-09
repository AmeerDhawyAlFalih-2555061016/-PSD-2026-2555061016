class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True

        return False

    def search(self, key):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (
                self.table[i].state == SlotState.OCCUPIED
                and self.table[i].key == key
            ):
                return self.table[i]

        return None

    def remove_key(self, key):
        entry = self.search(key)

        if entry is None:
            return False

        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\n=== LEADERBOARD ARENA PvP LEGENDARIS ===")

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")

            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")

            else:
                print(
                    f"(Player ID: {self.table[i].key}, "
                    f"Win: {self.table[i].value})"
                )


def main():
    leaderboard = HashMapOpenAddressing()

    leaderboard.insert(1001, 25)
    leaderboard.insert(1011, 17)
    leaderboard.insert(1021, 33)
    leaderboard.insert(1002, 12)

    print("Data pemain berhasil ditambahkan.")
    leaderboard.display()

    hasil = leaderboard.search(1011)

    if hasil is not None:
        print(
            f"\nPlayer ID 1011 ditemukan "
            f"dengan jumlah kemenangan = {hasil.value}"
        )
    else:
        print("\nPlayer ID 1011 tidak ditemukan")

    hasil = leaderboard.search(1021)

    if hasil is not None:
        print(
            f"\nPlayer ID 1021 ditemukan "
            f"dengan jumlah kemenangan = {hasil.value}"
        )

    leaderboard.display()

    leaderboard.remove_key(1011)

    print("\nSetelah menghapus Player ID 1011:")
    leaderboard.display()

    hasil = leaderboard.search(1021)

    if hasil is not None:
        print(
            f"\nPlayer ID 1021 masih ditemukan "
            f"dengan jumlah kemenangan = {hasil.value}"
        )
    else:
        print("\nPlayer ID 1021 tidak ditemukan")


if __name__ == "__main__":
    main()