# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Recommendation systems are built based on approaches namely content-based filtering and collaborative filtering. Content based filtering solely focuses on the metadata or the attributes of the items to be recommended and the preference of the user. There are no user-item interaction history in this approach. Although, it might not provide us with more accurate recommendations, this approach doesn't require larger dataset and works best when there are no user-item interaction data or to tackle cold-start problem. 

Collaborative filtering on the other hand solely depends on the user's interactions with features/items within the system. Two major approach to collaborative filtering are Item-Item based and User-User based collaborative filtering. Item-item based filtering focuses on items a user have interacted most with such as liked, added to the playlist, saved to the library in the past and compares similar items to the user's liking to be recommeded. While user-user based filtering finds similar users based on their interaction history and recommends items top similar users have liked for our given user.

In our project, we don't have access to user interaction history and have rather smaller dataset to work with. Given the limitations, our project will focus on implementing content-based filtering to recommend songs to a user. User have their preference listed in their profile which highlights the genre, mood, energy and whether the user likes acoustic songs or not. Similarly, songs have similar attributes in their song. We will use the user preference and song attributes to recommend top k songs to our user.

Some prompts to answer:

- What features does each `Song` use in your system?

  As user preference provides favorite_genre, favorite_mood, target_energy, and likes_acoustic or not boolean value as attributes, we will use genre, mood, energy and acousticness features of the song to use in our recommender systems.
  
- What information does your `UserProfile` store?

  UserProfile has user preferences namely favorite_genre, favorite_mood, target_energy, and likes_acoustic.

- How does your `Recommender` compute a score for each song?

  For each song, the feature of the song and user preference are compared based on if they are matched. Genre, mood, energy and acousticness have weights assigned in non-incremental order from 20, 15, 15, and 10 if each values match the user preference. The final score is summation of all the scores for each feature.

- How do you choose which songs to recommend?

  In order to add diversity to the recommendation, we will approach the recommendation with 80% similarity and 20% discovery. Among top K, 80% will be highest ranked and the 20% will be the lowest ranked songs. The recommendation also ensures all the songs are from different artists to promore exploration.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

