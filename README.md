# Habit Tracker

#### Video Demo: https://youtu.be/YcCcORI4C8w

#### Description:

Habit Tracker is a full-stack web application designed to help users build, manage, and maintain daily habits through consistent tracking and visual feedback. The purpose of the project is to make habit formation more structured and motivating by allowing users to clearly see their progress over time, rather than relying on memory or external tools such as spreadsheets or notes.

The application begins with a user authentication system that allows individuals to register for an account and securely log in. Each user has their own isolated data, meaning habits, progress, and completion history are stored separately and are not accessible by other users. This ensures a personalized experience and prevents data overlap. Authentication is an essential part of the project because habit tracking is inherently personal, and users need a secure way to store and retrieve their data across sessions.

Once logged in, users are taken to the main dashboard page (index page), which serves as the central hub for daily habit interaction. On this page, each habit is displayed as an individual card. These cards provide quick access to the most important actions: marking a habit as completed for the current day or undoing a completion if it was recorded by mistake. This design prioritizes simplicity and encourages daily engagement without overwhelming the user with unnecessary options.

The index page also includes a progress bar that visually represents how many habits have been completed on a given day compared to the total number of active habits. In addition to the progress bar, users can see a numerical summary showing the total number of active habits and how many have been completed on the current day. These features are intended to provide immediate feedback and motivation, helping users understand their daily performance at a glance.

Another core feature of the application is the “Manage Habits” page, which allows users to fully control their habit list. From this page, users can create new habits, assign tags for categorization, rename existing habits, or delete habits they no longer want to track. Tags help users organize their habits into meaningful groups such as health, productivity, or study. This makes it easier to manage multiple habits and maintain clarity as the number of tracked habits grows. The ability to rename and delete habits ensures that the system remains flexible and adaptable to changing goals over time.

In addition to daily tracking, the application includes a “Dashboard” page that focuses on long-term progress visualization. This page displays a calendar-style grid representing the current month. Each row corresponds to a specific habit, while each column represents a day of the month. When a habit is completed on a specific day, the corresponding cell is highlighted or colored, creating a visual map of the user’s consistency. This design allows users to quickly identify patterns such as streaks, missed days, or improvement over time. Unlike the main page, which focuses on daily interaction, the dashboard emphasizes reflection and long-term behavior analysis.

The backend of the application is built using Flask, which handles routing, user sessions, and server-side logic. SQLite is used as the database to store user accounts, habits, and completion records. The database structure is designed to efficiently link users to their habits and track completion history on a per-day basis. Jinja templates are used to dynamically render HTML pages based on user-specific data, ensuring that each user sees only their own habits and progress.

On the frontend, the application uses HTML, CSS, and JavaScript to create an interactive and responsive user interface. CSS is used to style habit cards, progress indicators, and the dashboard grid in a way that is both functional and visually clear.

One of the key design goals of this project was to balance simplicity with functionality. Many habit-tracking applications can become overly complex, which discourages regular use. To avoid this, the interface was intentionally kept minimal, focusing only on the actions users need most: adding habits, completing them, and reviewing progress. At the same time, the dashboard provides a deeper analytical layer for users who want to reflect on their long-term behavior.

Overall, Habit Tracker demonstrates concepts such as user authentication, CRUD operations, relational database design, and dynamic frontend-backend interaction. It was built as a practical tool to solve a real-world problem: maintaining consistency in personal habits through clear feedback and structured tracking.


## Features

### User Authentication
- Users can register a new account and log in.
- Each user's habits and progress are stored separately.
- Users can log out when they are finished.

### Home Page (`index.html`)
The home page provides an overview of the user's current habits. It includes:
- Habit cards displaying each active habit.
- The ability to mark a habit as completed for the day.
- The ability to undo a completion if a habit was marked accidentally.
- A progress bar showing daily completion progress.
- A total habit count.
- A count of how many habits have been completed today.

### Manage Habits Page
The Manage Habits page allows users to organize their habits. Users can:
- Create new habits.
- Assign tags to habits for categorization.
- Rename existing habits.
- Delete habits they no longer want to track.

### Dashboard Page
The Dashboard provides a visual history of habit completion:
- Displays habits in a monthly calendar-style table.
- Each row represents a habit.
- Each column represents a day of the current month.
- Completed days are visually highlighted, making it easy to identify consistency and patterns over time.

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite
- Jinja templates

## Design Choices

I chose to build a habit tracker because maintaining consistency with personal goals can be difficult without a clear way to measure progress. The application focuses on making daily tracking simple while also providing a long-term view of improvement through the dashboard.

The calendar-style dashboard was designed to help users recognize patterns in their habits, such as streaks and missed days, instead of only focusing on individual completions.

## Author

Created by: Dariia Burtseva
