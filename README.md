
# Generative AI API

Rest API made by Flask, for generative AI model used for Skin Match App.

## Deploy Link
Deploy Link : https://my-genai2-model-dczyyawmja-et.a.run.app

## Setup

Here is how to setup the api to run locally on your computer.


**1. Make Environment on Your Local Computer**

On cmd, use this command:
```bash
  cd "your/folder/project/path"
```
```bash
  python venv env
```
```bash
  cd env
```
```bash
  cd Scripts
```
```bash
  cd Activate.bat
```
Go in to your project folder directory
```bash
  cd ..
```
```bash
  code .
```


**2. Clone This Repository and Customize**

a. Change the project ID and location according to your own project.

b. Go to your GCP, make a service account with roles of:
```bash
  Vertex AI User
  Storage Object Viewer
```
c. Get the key in json.

d. Save the key in credential folder, or any seperate folder.

e. Change the credential path in the app.py.


**3. Install Dependencies**
```bash
    pip install -r requirements.txt
```


**4. Run**
```bash
    python app.py
```


## Generative AI

* Endpoint:
    * `POST /predict`

* Request Body: 
```json
{
  "skin_type": "oily",
  "skin_concerns": "hyperpigmentation, acne",
  "current_skincare": "serum"
}
```
* Response:
```json
{
    "result": "## Skincare Routine for Oily Skin with Hyperpigmentation and Acne:\n\n**Congratulations on taking the first step towards a clearer, brighter complexion!** Oily skin with hyperpigmentation and acne can be challenging, but with the right routine, you can achieve a healthy glow. Here's a tailored plan for you:\n\n**Morning:**\n\n1. **Cleanse:** Start with a gentle, oil-free cleanser. Look for ingredients like salicylic acid or glycolic acid to help control oil production and exfoliate dead skin cells. Avoid harsh soaps or scrubs that can irritate your skin.\n2. **Treat:** Apply a serum with vitamin C to brighten hyperpigmentation and boost collagen production. Look for a serum with a high concentration of L-Ascorbic Acid (vitamin C) for optimal results.\n3. **Moisturize:** Use a lightweight, oil-free moisturizer with SPF 30 or higher. This will hydrate your skin without clogging pores and protect it from sun damage, which can worsen hyperpigmentation.\n4. **Spot Treat:** If you have active acne, apply a spot treatment with benzoyl peroxide or salicylic acid to the affected areas.\n\n**Evening:**\n\n1. **Double Cleanse:** Remove makeup and impurities with an oil-based cleanser followed by a water-based cleanser. This ensures a thorough clean without stripping your skin of its natural oils.\n2. **Exfoliate:** 2-3 times a week, use a chemical exfoliant with glycolic acid or salicylic acid to remove dead skin cells and prevent clogged pores.\n3. **Treat:** Apply a serum with retinol or niacinamide to address hyperpigmentation and acne. Retinol can be drying, so start with a low concentration and gradually increase as your skin tolerates it. Niacinamide is a gentler option that can also help control oil production.\n4. **Moisturize:** Use a lightweight, oil-free moisturizer.\n5. **Spot Treat:** Apply a spot treatment as needed.\n\n**What to Avoid:**\n\n* **Heavy creams and oils:** These can clog pores and worsen acne.\n* **Harsh scrubs:** These can irritate your skin and make hyperpigmentation worse.\n* **Fragrances and dyes:** These can irritate sensitive skin.\n* **Over-exfoliating:** Exfoliating too often can damage your skin barrier and make it more prone to breakouts.\n* **Picking or squeezing pimples:** This can lead to scarring and infection.\n\n**Additional Tips:**\n\n* **Drink plenty of water:** Staying hydrated is essential for healthy skin.\n* **Eat a balanced diet:** Avoid processed foods and sugary drinks, which can contribute to acne.\n* **Manage stress:** Stress can trigger acne breakouts. Find healthy ways to manage stress, such as exercise or meditation.\n* **Be patient:** It takes time to see results from a skincare routine. Be consistent and don't give up!\n\n**Remember:** This is a general guideline. It's always best to consult with a dermatologist or licensed esthetician for personalized advice based on your specific skin concerns. They can help you create a customized skincare routine that addresses your individual needs. \n"
}
```
