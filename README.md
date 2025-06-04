# Zus Health Test

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
[![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
[![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)

A small project for the Zus Health test.

Just a small Python class and FastAPI script with a simple React page
![alt text](https://github.com/tjaung/Zushealth_test/blob/main/preview.png?raw=true)

# Installation

[(Back to top)](#table-of-contents)

To clone the project:

```shell
git clone git@github.com:tjaung/Zushealth_test.git # ssh
git clone https://github.com/tjaung/Zushealth_test.git # https
```

# Usage

[(Back to top)](#table-of-contents)

Contains both client and server side code. To see the server side, go into server.

```
cd server
python3 -m venv venv # create virtual environment
source venv/bin/activate # start virtual environment
pip3 install requirements.txt # install requirements
```

To run tests, run:

```
pytest
```

# Assignment

Symmetric Key Distribution Problem:

When you’ve got to plan a communication strategy for a private network, one challenge is
figuring out how to allocate private (aka symmetric) keys so that all the people who use a
network can communicate, but no one has a key they shouldn’t have. The rules for this are:
- Each person in the network plan will have at least one device. Assume that no two
people share a device.
- Each device has a unique ID, and can hold a number of keys. How many is particular to
the device. To start, assume each device can hold 4 keys. The key positions are called
slots and are numbered, starting from 1.
- A network is the set of devices used by a set of people who must be able to
communicate simultaneously. A network must have exactly 1 symmetric key, so that all
people can decrypt whatever is sent to the network.
- A key (aka symmetric key) should be on only 1 network.

Given a set of networks and unique names of people, your code should report the list keys to be
set up, and give instructions on how to set up each device. It should also eliminate any
duplicates, in case the network plan is redundant.
Example:

- Assume we’ve got 4 people in this example - Alice, Bob, Carlos, and David.
- Alice and Bob need to have a private channel between the two of them
- Alice and Carlos need to have a private channel between the two of them
- Alice and David need to have a private channel between the two of them
- All four people must communicate, there must be a network between Alice, Bob, Carlos,
and David
- Bob, Carlos and David must have a network that excludes Alice.
- Bob, Alice need to have a private channel between the two of them

For this situation, the output should be:

Network 1, key 1  
- Alice - put key 1 in slot 1
- Bob - put key 1 in slot 1

Network 2, key 2  
- Alice - put key 2 in slot 2
- Carlos - put key 2 in slot 1 (any slot, it doesn’t matter, as long as there is no
repeat)

Network 3, key 3  
- Alice - put key 3 in slot 3
- David - put key 3 in slot 1 (any slot, it doesn’t matter, as long as there is no
repeat)

Network 4, key 4  
- Alice - put key 4 in slot 4
- Bob - put key 4 in slot 2
- Carlos - put key 4 in slot 2
- David - put key 4 in slot 2
  
Network 5, key 5  
- Bob - put key 5 in slot 3
- Carlos - put key 5 in slot 3
- David - put key 5 in slot 3

And you don’t need a 6th network because Bob, Alice = Alice, Bob
Error case:

Assuming all the networks in the original example, if Alice, Bob and Carlos must communicate
(omitting David) - the system should now throw an error. Alice’s device does not have room for
a 5th key. So an error like “Error! Alice’s device is out of keys” should be thrown.

Assignment:
Please implement a key distribution tool.
It should be able to take a network plan that is a list of sets of names, give 1 device (4 slots) to
each person, and then write out the key distribution plan as shown in the example or give an
error if the distribution plan can’t be done giving a single device for each person.
Sample input from the example:
(Alice, Bob), (Alice, Carlos), (Alice, David), (Alice, Bob, Carlos, David)
Where each () is a network.

If you have extra time remaining in the suggested 2 hour limit, consider adding one or more of
the following to the project:
- An interaction to allow defining the initial network.
- Automated testing
- Convert this to a service (e.g. an API) which is deployed to a cloud provider.
- Any other feature that allows you to show off your software engineering skills.
Guidelines for candidates:
- Use a programming language of your choice
- Be prepared to explain the decisions you made and
- Be prepared to demonstrate this code on a Zoom meeting and potentially make
changes.

For Client side, go to client folder from root

```
cd client
npm i # install requirements
npm run dev # start
```
