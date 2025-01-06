import pygame

class InventoryManager:
    def __init__(self):
        self.inventories = {}
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Inventory Manager')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('timesnewroman', 14)
        self.running = True
        self.backpack_slots = [None] * 10
        self.equipped_items = {
            "head": None, "face": None, "left_ear": None, "right_ear": None,
            "neck": None, "second_neck": None, "back": None, "shoulders": None,
            "chest": None, "arms": None, "wrists": None, "hands": None,
            "right_hand": None, "left_hand": None, "fingers": [None] * 10,
            "waist": None, "legs": None, "feet": None
        }

    def add_item(self, username, item):
        if username not in self.inventories:
            self.inventories[username] = []
        self.inventories[username].append(item)
        return f"Added {item} to {username}'s inventory."

    def remove_item(self, username, item):
        if username in self.inventories and item in self.inventories[username]:
            self.inventories[username].remove(item)
            return f"Removed {item} from {username}'s inventory."
        return f"Item {item} not found in {username}'s inventory."

    def view_inventory(self, username):
        if username in self.inventories:
            return self.inventories[username]
        return f"{username} has no inventory."

    def draw_inventory(self):
        self.screen.fill((0, 0, 0))
        # Draw backpack slots
        for i in range(10):
            pygame.draw.rect(self.screen, (255, 255, 255), (50 + i * 70, 50, 60, 60), 2)
            label = self.font.render(f"SLOT {i+1}", True, (255, 255, 255))
            self.screen.blit(label, (50 + i * 70, 30))
            if self.backpack_slots[i]:
                item_text = self.font.render(self.backpack_slots[i].upper(), True, (255, 255, 255))
                self.screen.blit(item_text, (55 + i * 70, 65))

        # Draw equipped items slots with labels
        slot_positions = {
            "head": (120, 150), "face": (190, 150), "left_ear": (50, 150), "right_ear": (260, 150),
            "neck": (120, 240), "second_neck": (190, 240), "back": (50, 240), "shoulders": (260, 240),
            "chest": (190, 330), "arms": (120, 330), "wrists": (50, 330), "waist": (260, 330),
            "right_hand": (50, 420), "left_hand": (190, 420), "hands": (120, 420),
            "legs": (120, 510), "feet": (190, 510)
        }
        for slot, (x, y) in slot_positions.items():
            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 60, 60), 2)
            label = self.font.render(slot.replace('_', ' ').upper(), True, (255, 255, 255))
            self.screen.blit(label, (x, y - 20))
            if self.equipped_items[slot]:
                item_text = self.font.render(self.equipped_items[slot].upper(), True, (255, 255, 255))
                self.screen.blit(item_text, (x + 5, y + 25))

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_inventory()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    manager = InventoryManager()
    manager.run()