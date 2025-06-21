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
- [**Command Pattern**](#command-pattern) – for encapsulating user actions like sending messages or submitting join requests.

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

## How It Works

# References
🔗 [Observer Pattern – Refactoring.Guru](https://refactoring.guru/design-patterns/observer)

