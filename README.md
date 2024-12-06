# Investment Manager 

## 📋 Overview

This project is a **Desktop Application** designed to help users manage and monitor the return on their investments. The app consists of two main components:

1. **Frontend**: A desktop application built using [Flet](https://flet.dev/).
2. **Backend**: A RESTful API server built with **Node.js**, **TypeScript**, and **Drizzle ORM**, connected to a **PostgreSQL** database.

---

## 🖥️ Desktop App (Frontend)

The desktop app provides an intuitive interface for:

- **Managing Investments**: Add, update, or delete investments.
- **Calculating Returns**: View the profit or loss percentage for each investment.
- **Visualizing Data**: Display mock data and real-time information on investment performance.
### Key Features
<!-- - **Tabs for Navigation**: Easy-to-use tab-based UI to navigate between functionalities. -->
- **Dynamic Calculations**: Automatically calculate and display investment returns.
- **Data Visualization**: Highlight profit or loss percentages with green (profit) or red (loss).

---

## 🌐 Server (Backend)

The backend server is responsible for:

- **Investment Data Management**: Store and retrieve investment data from a **PostgreSQL** database.
- **Endpoints for CRUD Operations**:
  - Create, Read, Update, and Delete investments.
- **Real-Time Sync**: Provide real-time data updates for the desktop app.

### Built With
- **Node.js**: Backend runtime for building the server.
- **TypeScript**: Strongly typed JavaScript for robust development.
- **Drizzle ORM**: Lightweight and flexible ORM for database interaction.
- **PostgreSQL**: Relational database to store user investments.

---

<!-- ## 🛠️ Installation & Setup -->
<!---->
<!-- ### Prerequisites -->
<!-- - **Node.js** (v18+) -->
<!-- - **Bun** (package manager) -->
<!-- - **PostgreSQL** -->
<!---->
<!-- ### Clone the Repository -->
<!-- ```bash -->
<!-- git clone <repository-url> -->
<!-- cd <repository-name> -->
