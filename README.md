# Problem statement
You are asked to be a data analyst for Magical Hair, your local hairdresser. They already have some data but would like
to get some insights into what that data can tell them.

The exercises are provided in `src/exercises.py`. We start you off with some data. The exercises are provided through
the triple quoted strings, explaining what is asked of you.

Please refer to the email you received from Share Network on the details and the submission deadline.

# Getting started
## Git repository
Follow these steps to get your Git repository ready to go:
1. You can copy the repository to your own account by clicking "Fork":
   ![image](https://github.com/user-attachments/assets/4dd2d24b-ddfe-4a36-933f-a7444700f4b9)
2. Go to your forked repository and **set it to private** (see [GitHub documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility) for how to do this). Make
   sure to invite Share Network (see the email you received).
3. Clone the forked repository to your local computer. If you have trouble with this, please see the official GitHub
   documentation or ask your mentor.
   - Advanced: GitHub also allows for using "Codespaces", where you can code within GitHub. See
     [their documentation](https://docs.github.com/en/codespaces) for more information. Note that we have not tested this.

## Python environment
Here are the steps to follow to set up this repo in your local development environment (assuming you are not using
[GitHub codespaces](https://docs.github.com/en/codespaces) as described above).
1. Set up your IDE. For example, when using VSCode, see [this YouTube video](https://www.youtube.com/watch?v=D2cwvpJSBX4).
2. Open the cloned repository in your IDE.
3. If you have not yet installed `uv` on your computer, follow the instructions [in their documentation](https://docs.astral.sh/uv/getting-started/installation/).
   We recommend using the `pipx` installation process.
4. In a terminal window for your repository (e.g. on VSCode, click the "Terminal" menu at the top and then click
   "New terminal"), create the virtual environment with all necessary packages with `uv sync --all-groups`.
5. You are ready to go! Try to run `src/exercises.py`. If everything went correctly, you will see that it prints
   `"Data generated correctly! 🚀"` and the start of the data.

Good luck!

## Generating the data
You can generate some data through this code:
```python
import datetime
import generate_data

customer_specs = generate_data.CustomerSpecs(num_customers=1_000, min_age=12, max_age=80)
order_specs = generate_data.OrderSpecs(num_orders_per_day=20, start_date=datetime.date(2024, 1, 1), end_date=datetime.date(2024, 12, 31))
data_string = generate_data.main(customer_specs=customer_specs, order_specs=order_specs, seed=1234)
```

Feel free to play with it yourself as well, for example making more days of data by modifying `start_date` and/or
`end_date` in `generate_data.OrderSpecs`, or adding more customers by increasing `num_customers` in
`generate_data.CustomerSpecs`.

# Ideas for more exercises
If you finish early, or you feel like you want to pick up a bit more, here are some ideas for you or your mentor to
explore for further exercises:
- Knowing syntax: Ask your mentor to give you a script that does not work, e.g. with syntax issues. Then, you fix it.
- Modifying data: You can add more hairstyles, add other constraints to the data, or add more columns/fields.
- Making data yourself: Create a reservation system, what data do you need?
- Data engineering: The data is now one big list of customers and orders. However, it is good practice to split up
  the data, for example into a "customers" dataset and an "orders" dataset. How can you split the existing data into
  these two datasets?
- Data analytics/science:
  - You can use the `pandas` library to make the exercises again but with `DataFrames` instead of lists.
  - You can compute many more descriptive statistics with e.g. groupby. For example, exercise 4.4 is suitable.
  - You can make some plots, for example to plot the revenue over time.
  - You can do a simple linear regression to predict, for example, revenue.
- You can always check the [cheatsheet](https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet) to see if there are uncovered items that you would like to practice.

# Questions?
Can you not figure out an exercise yourself? Then do the following:
1. Check the [Codecademy cheatsheet](https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet) for inspiration.
2. You can check `src/solutions/sample_solutions.txt` for an idea of what the answer should look like. Note that this is
   generated on a much smaller subset of data, so the values do not represent what your answer should be. It is only
   about the structure of the output.
3. When an exercise relies on previous results, we have added an `import` statement with temporary data so you can
   continue. Use the provided temporary data to continue with the next exercise. When the exercise is fixed, remove the
   temporary data and check that the rest of your solutions still work.
4. When you next meet your mentor, ask them for help.

Do you have questions not related to the content of these exercises? Then contact Share Network.
