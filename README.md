# Digital Room Service & Guest Portal

A responsive, Django-powered web application designed to automate hotel room service workflows and manage live inventory tracking. This project serves as a fully functional prototype simulation, demonstrating how manual hospitality operations can be digitized to improve efficiency and secure data privacy.

---

## 🚀 System Workflow

The application operates as a 4-step user journey:
1. **Guest Check-in:** The guest enters their stay details, establishing a secure, isolated session.
2. **Browse Menu:** The portal dynamically fetches live item availability from the database.
3. **Place Order:** The backend validates stock levels, reduces inventory counts in real time, and updates the bill.
4. **Checkout:** The system generates an error-free, itemized final total and securely terminates the session.

---

## 🛠️ Tech Stack

* **Backend Engine:** Python & Django (Routing & Core Logic)
* **Database Structure:** SQLite (Inventory & Order Management via Django ORM)
* **Data Security:** Django Sessions (Temporary user data isolation)
* **User Interface:** Bootstrap, HTML5, CSS3 (Responsive Design)

---

## ✨ Key Advantages

* **Zero Manual Paperwork:** Completely replaces front-desk logging with an automated digital workflow.
* **Overselling Prevention:** Built-in backend arithmetic instantly blocks menu selections when stock counts reach zero.
* **Absolute Privacy:** Session-based tracking ensures guest data never overlaps or persists post-checkout.
* **100% Bill Accuracy:** Eliminates calculation errors by automating line-item totals.

---

## ⚠️ Prototype Limitations

* **Local Hosting Only:** Currently operates in a local sandbox (`localhost`) environment.
* **Simulated Payments:** Calculates and displays transactional totals but lacks integration with a live credit card payment gateway.
* **Basic Text UI:** Leverages clean text layouts instead of a rich, dynamic image gallery for room service items.

---

## 🔮 Future Enhancements

* **Cloud Deployment:** Migrating the local architecture to a live hosting platform like AWS or Heroku.
* **Payment Gateway Integration:** Incorporating API endpoints for real-world transactions via Stripe or PayPal.
* **Dynamic Media Gallery:** Transitioning to a media-rich interface featuring dynamic image uploads for all menu listings.

---

## 📦 Installation & Setup

To run this simulation locally, ensure you have Python installed and follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/digital-room-service-guest-portal.git](https://github.com/YOUR_GITHUB_USERNAME/digital-room-service-guest-portal.git)
   cd digital-room-service-guest-portal
