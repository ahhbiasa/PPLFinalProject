<p align="center"><b>Software Design Final Project (2025)</b><br>Institute Teknologi Sepuluh Nopember</p>

<p align="center">
  <img src="./Lambang-ITS-2.png" alt="ITS" width="350"/>
</p>

<p align="center">Design Pattern implementation to our Final Project that was created for <a href="https://www.its.ac.id/informatika/wp-content/uploads/sites/44/2023/11/Module-Handbook-Bachelor-of-Informatics-Program-ITS.pdf">ER234301</a>.</p>
<p align="center">All codes were created by <a href="https://github.com/ahhbiasa">Abhyasa</a> and <a href="https://github.com/clistdy">Callista</a></p>

<div align="center">

| Name                    | NRP        |
|-------------------------|------------|
| Muhammad Abhyasa Santoso | 5025221066 |
| Tabina Callistadya        | 5025221318 |

</div>


<hr>

# Project Overview
**UCollabs** is a web-based collaboration platform developed for students at Universiti Teknologi Petronas (UTP). It allows students to connect, post projects, and find suitable teammates for academic or creative work. Our final project simulates core functionality such as posting collaboration requests and sending real-time notifications.

  <p align="center">
    <img src="./UCollabs_Logo.png" alt="UCollabs" width="300"/>
  </p>

To support this functionality in a clean, scalable way, we have applied two software design patterns:

- [**Observer Pattern**](#observer-pattern) – for handling real-time updates and notifications.
- [**Command Pattern**](#command-pattern) – for encapsulating user actions when submitting join requests or cancel requests.

# Observer Pattern
<p align="center">
  <img src="https://refactoring.guru/images/patterns/content/observer/observer-2x.png" width="400">
</p>

The **Observer Design Pattern** is a behavioral design pattern that creates a one-to-many object dependency. As the state of the **Subject (or Observable)** is altered, all its **Observers** are notified and updated automatically. This pattern is ideal when multiple objects need to react to changes in another object without tightly coupling them. Common in event-driven systems, GUIs, and real-time data feeds. The following is an analogy of why the observer pattern can be useful.

## The Problem
Imagine a customer awaiting the release of a new product at a store.

<p align="center">
  <img src="https://refactoring.guru/images/patterns/content/observer/observer-comic-1-en.png?id=1ec8571b22ea8fd2ed537f06cc763152">
<p/>

The customer can visit the store every day to look, but that’s tiring and essentially useless if the product isn’t out yet. Or, the store can email all the customers when they receive a new product in, but that may frustrate those who are not interested.

An issue rises where either the customer wastes time checking, or the store is spamming uninterested people. We need a smarter way of keeping prospects informed without bothering the rest. But how can we resolve this issue?

## Solution
This structure is exactly where the Observer Pattern becomes useful, it enables customers to "subscribe" to notifications so that the store only notifies the interested parties.

<p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/observer/solution1-en.png?id=60fb9a2822649dec1c68b78733479c57">
</p>

A publisher can notify only the subscribers who care about certain updates:
- The store becomes a publisher, and anyone who wants updates on a product becomes a subscriber.
- The store keeps a list of subscribers and gives them the option to subscribe or unsubscribe anytime.
- When something important happens (like a new product arriving), the store loops through its list and calls an update method on each subscriber to notify them.

This way:
- Only interested customers get notified
- The store doesn’t waste time or resources reaching out to everyone
- New types of subscribers can join in later without changing the store’s code.

To keep things clean and flexible, all subscribers follow the same interface. The store talks to subscribers through this interface without knowing what kind of object they are. That keeps the system loosely coupled and easy to expand

## Implementation
A simple Python prototype demonstrating the implementation of the Observer Pattern can be found [here](https://github.com/ahhbiasa/PPLFinalProject/tree/main/ucollabs_observer).

# Command Pattern
<p align="center">
  <img src="https://refactoring.guru/images/patterns/content/command/command-en-2x.png" width="400">
</p>

The **Command Design Pattern** is a behavioral design pattern that wraps an action or request into its own object. This makes it possible to pass the request as an argument, delay when it gets executed, organize it in a queue, or even reverse the action through an undo feature. This pattern is especially helpful in UCollabs when implementing user actions that must be reversible, like joining or withdrawing from a project collaboration request before it is approved. 
 
## The Problem
Imagine, building one of the feature for UCollabs which is "Join a Project" where students can browse available projects and click a “Join” button to request collaboration. Later, the student might want to cancel that request before it gets accepted so they hit the "Cancel" button which refers to undo action.

<p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/command/problem2-2x.png" width="400">
</p>

At first, you might think, “Easy! Just add the join and cancel logic directly to the button handler.” But then you realize, the same action (like joining a project) might be triggered from multiple places, maybe a button on the homepage, inside the project detail view, or even from a mobile version of the app if there's a mobile version later. 

<p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/command/problem3-en-2x.png" width="400">
</p>

If you write the logic for joining in every button or page, you’re copying the same code everywhere. That’s messy and hard to maintain. Or, What if you want to add an undo feature? Or store a history of what users did?

## Solution
In good software design, it's important to keep different responsibilities separate. For example, separating the part of the system that handles how things look (the interface) from the part that actually does the work (the logic). The interface shouldn’t directly handle the logic for what happens when a user joins or cancels a project. Instead, the system should delegate that responsibility to a separate, reusable part of the code.

<p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/command/solution1-en-2x.png" width="400">
</p>

This is where the Command Pattern helps. It allows us to wrap the “join project” action as a command object. This object knows how to execute (join the project) and undo (cancel the request). With the Command Pattern, every action a user takes like “join project” is turned into its own command object. This object knows exactly what to do (join) and how to undo it (cancel).

<p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/command/solution2-en-2x.png" width="400">
</p>

The UI just calls the command, without needing to know the technical details of how the action is performed.

<p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/command/solution3-en-2x.png" width="400">
</p>

This way:
- The UI buttons don’t need to know how a project join works.
- The join logic is reusable and testable on its own.
- We can easily add undo functionality.
- We avoid duplicating logic across different parts of the app (buttons, menus, etc.).

The Command Pattern acts as a smart middle layer between the user interface and the business logic — reducing direct connections and making the whole system easier to manage.

## Implementation
A simple Python prototype demonstrating the implementation of the Command Pattern can be found [here](https://github.com/ahhbiasa/PPLFinalProject/tree/main/ucollabs_command).

## How It Works

# References
🔗 [Observer Pattern – Refactoring.Guru](https://refactoring.guru/design-patterns/observer)
🔗 [Command Pattern – Refactoring.Guru](https://refactoring.guru/design-patterns/command)

