import random
from app.models import Mobile, Manufacturer
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate the database with dummy Mobile and Manufacturer data"

    def handle(self, *args, **kwargs):
        # Lists of predefined data
        mobile_names = [
            "Galaxy S21", "iPhone 13", "Pixel 6", "Xiaomi Mi 11", "OnePlus 9",
            "Nokia XR20", "Sony Xperia 1 III", "Motorola Edge 20", "Oppo Find X3", "Huawei P50"
        ]
        descriptions = [
            "A powerful and modern smartphone.",
            "Perfect for photography enthusiasts.",
            "Flagship model with cutting-edge technology.",
            "Affordable phone with high-end features.",
            "The ultimate gaming experience.",
            "Compact and durable for everyday use.",
            "Elegant design with superior performance.",
            "Innovative features packed in a sleek body.",
            "Premium phone at a reasonable price.",
            "Top-notch camera and performance."
        ]
        manufacturer_names = ["Samsung", "Apple", "Google", "Xiaomi", "OnePlus", "Nokia", "Sony", "Motorola", "Oppo", "Huawei"]

        # Create Manufacturer objects
        self.stdout.write("Creating manufacturers...")
        manufacturers = []
        for name in manufacturer_names:
            manufacturer, created = Manufacturer.objects.get_or_create(
                title=name,
                defaults={"description": f"{name} is a leading mobile phone manufacturer."}
            )
            if created:
                self.stdout.write(f"Manufacturer {name} created.")
            manufacturers.append(manufacturer)

        # Create Mobile objects
        self.stdout.write("Creating mobiles...")
        for _ in range(10):  # Create 10 mobiles
            Mobile.objects.create(
                ram=random.uniform(2.0, 12.0),  # Random RAM between 2GB and 12GB
                cpu=f"CPU-{random.randint(1000, 9999)}",  # Random CPU identifier
                title=random.choice(mobile_names),
                description=random.choice(descriptions),
                manufacturer=random.choice(manufacturers),  # Random manufacturer
                status=random.choice(['0', '1']),  # Random status
            )

        self.stdout.write(self.style.SUCCESS("Dummy data for Mobiles and Manufacturers created successfully!"))