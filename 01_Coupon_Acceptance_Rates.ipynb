{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Will a Customer Accept the Coupon?\n",
    "\n",
    "**Context**\n",
    "\n",
    "Imagine driving through town and a coupon is delivered to your cell phone for a restaraunt near where you are driving. Would you accept that coupon and take a short detour to the restaraunt? Would you accept the coupon but use it on a sunbsequent trip? Would you ignore the coupon entirely? What if the coupon was for a bar instead of a restaraunt? What about a coffee house? Would you accept a bar coupon with a minor passenger in the car? What about if it was just you and your partner in the car? Would weather impact the rate of acceptance? What about the time of day?\n",
    "\n",
    "Obviously, proximity to the business is a factor on whether the coupon is delivered to the driver or not, but what are the factors that determine whether a driver accepts the coupon once it is delivered to them? How would you determine whether a driver is likely to accept a coupon?\n",
    "\n",
    "**Overview**\n",
    "\n",
    "The goal of this project is to use what you know about visualizations and probability distributions to distinguish between customers who accepted a driving coupon versus those that did not.\n",
    "\n",
    "**Data**\n",
    "\n",
    "This data comes to us from the UCI Machine Learning repository and was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. Answers that the user will drive there ‘right away’ or ‘later before the coupon expires’ are labeled as ‘Y = 1’ and answers ‘no, I do not want the coupon’ are labeled as ‘Y = 0’.  There are five different types of coupons -- less expensive restaurants (under \\\\$20), coffee houses, carry out & take away, bar, and more expensive restaurants (\\\\$20 - \\\\$50). "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Deliverables**\n",
    "\n",
    "Your final product should be a brief report that highlights the differences between customers who did and did not accept the coupons.  To explore the data you will utilize your knowledge of plotting, statistical summaries, and visualization using Python. You will publish your findings in a public facing github repository as your first portfolio piece. \n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data Description\n",
    "Keep in mind that these values mentioned below are average values.\n",
    "\n",
    "The attributes of this data set include:\n",
    "1. User attributes\n",
    "    -  Gender: male, female\n",
    "    -  Age: below 21, 21 to 25, 26 to 30, etc.\n",
    "    -  Marital Status: single, married partner, unmarried partner, or widowed\n",
    "    -  Number of children: 0, 1, or more than 1\n",
    "    -  Education: high school, bachelors degree, associates degree, or graduate degree\n",
    "    -  Occupation: architecture & engineering, business & financial, etc.\n",
    "    -  Annual income: less than \\\\$12500, \\\\$12500 - \\\\$24999, \\\\$25000 - \\\\$37499, etc.\n",
    "    -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8\n",
    "    -  Number of times that he/she buys takeaway food: 0, less than 1, 1 to 3, 4 to 8 or greater\n",
    "    than 8\n",
    "    -  Number of times that he/she goes to a coffee house: 0, less than 1, 1 to 3, 4 to 8 or\n",
    "    greater than 8\n",
    "    -  Number of times that he/she eats at a restaurant with average expense less than \\\\$20 per\n",
    "    person: 0, less than 1, 1 to 3, 4 to 8 or greater than 8\n",
    "    -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8\n",
    "    \n",
    "\n",
    "2. Contextual attributes\n",
    "    - Driving destination: home, work, or no urgent destination\n",
    "    - Location of user, coupon and destination: we provide a map to show the geographical\n",
    "    location of the user, destination, and the venue, and we mark the distance between each\n",
    "    two places with time of driving. The user can see whether the venue is in the same\n",
    "    direction as the destination.\n",
    "    - Weather: sunny, rainy, or snowy\n",
    "    - Temperature: 30F, 55F, or 80F\n",
    "    - Time: 10AM, 2PM, or 6PM\n",
    "    - Passenger: alone, partner, kid(s), or friend(s)\n",
    "\n",
    "\n",
    "3. Coupon attributes\n",
    "    - time before it expires: 2 hours or one day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problems\n",
    "\n",
    "Use the prompts below to get started with your data analysis.  \n",
    "\n",
    "#### 1. Read in the `coupons.csv` file.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(r'C:\\Users\\agnek\\coupons.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>CoffeeHouse</th>\n",
       "      <th>CarryAway</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Restaurant(&lt;20)</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>2h</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Carry out &amp; Take away</td>\n",
       "      <td>2h</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>2h</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       destination  passanger weather  temperature  time  \\\n",
       "0  No Urgent Place      Alone   Sunny           55   2PM   \n",
       "1  No Urgent Place  Friend(s)   Sunny           80  10AM   \n",
       "2  No Urgent Place  Friend(s)   Sunny           80  10AM   \n",
       "3  No Urgent Place  Friend(s)   Sunny           80   2PM   \n",
       "4  No Urgent Place  Friend(s)   Sunny           80   2PM   \n",
       "\n",
       "                  coupon expiration  gender age      maritalStatus  ...  \\\n",
       "0        Restaurant(<20)         1d  Female  21  Unmarried partner  ...   \n",
       "1           Coffee House         2h  Female  21  Unmarried partner  ...   \n",
       "2  Carry out & Take away         2h  Female  21  Unmarried partner  ...   \n",
       "3           Coffee House         2h  Female  21  Unmarried partner  ...   \n",
       "4           Coffee House         1d  Female  21  Unmarried partner  ...   \n",
       "\n",
       "   CoffeeHouse CarryAway RestaurantLessThan20 Restaurant20To50  \\\n",
       "0        never       NaN                  4~8              1~3   \n",
       "1        never       NaN                  4~8              1~3   \n",
       "2        never       NaN                  4~8              1~3   \n",
       "3        never       NaN                  4~8              1~3   \n",
       "4        never       NaN                  4~8              1~3   \n",
       "\n",
       "  toCoupon_GEQ5min toCoupon_GEQ15min toCoupon_GEQ25min direction_same  \\\n",
       "0                1                 0                 0              0   \n",
       "1                1                 0                 0              0   \n",
       "2                1                 1                 0              0   \n",
       "3                1                 1                 0              0   \n",
       "4                1                 1                 0              0   \n",
       "\n",
       "  direction_opp  Y  \n",
       "0             1  1  \n",
       "1             1  0  \n",
       "2             1  1  \n",
       "3             1  0  \n",
       "4             1  0  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Investigate the dataset for missing or problematic data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 12684 entries, 0 to 12683\n",
      "Data columns (total 26 columns):\n",
      " #   Column                Non-Null Count  Dtype \n",
      "---  ------                --------------  ----- \n",
      " 0   destination           12684 non-null  object\n",
      " 1   passanger             12684 non-null  object\n",
      " 2   weather               12684 non-null  object\n",
      " 3   temperature           12684 non-null  int64 \n",
      " 4   time                  12684 non-null  object\n",
      " 5   coupon                12684 non-null  object\n",
      " 6   expiration            12684 non-null  object\n",
      " 7   gender                12684 non-null  object\n",
      " 8   age                   12684 non-null  object\n",
      " 9   maritalStatus         12684 non-null  object\n",
      " 10  has_children          12684 non-null  int64 \n",
      " 11  education             12684 non-null  object\n",
      " 12  occupation            12684 non-null  object\n",
      " 13  income                12684 non-null  object\n",
      " 14  car                   108 non-null    object\n",
      " 15  Bar                   12577 non-null  object\n",
      " 16  CoffeeHouse           12467 non-null  object\n",
      " 17  CarryAway             12533 non-null  object\n",
      " 18  RestaurantLessThan20  12554 non-null  object\n",
      " 19  Restaurant20To50      12495 non-null  object\n",
      " 20  toCoupon_GEQ5min      12684 non-null  int64 \n",
      " 21  toCoupon_GEQ15min     12684 non-null  int64 \n",
      " 22  toCoupon_GEQ25min     12684 non-null  int64 \n",
      " 23  direction_same        12684 non-null  int64 \n",
      " 24  direction_opp         12684 non-null  int64 \n",
      " 25  Y                     12684 non-null  int64 \n",
      "dtypes: int64(8), object(18)\n",
      "memory usage: 2.5+ MB\n"
     ]
    }
   ],
   "source": [
    "# General overview of data counts and data types \n",
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Duplicate Rows:\n",
      "     destination passanger weather  temperature  time                 coupon  \\\n",
      "4192        Work     Alone   Sunny           80   7AM  Carry out & Take away   \n",
      "4236        Work     Alone   Sunny           80   7AM  Carry out & Take away   \n",
      "4280        Work     Alone   Sunny           80   7AM  Carry out & Take away   \n",
      "4324        Work     Alone   Sunny           80   7AM  Carry out & Take away   \n",
      "4409        Work     Alone   Sunny           80   7AM  Carry out & Take away   \n",
      "...          ...       ...     ...          ...   ...                    ...   \n",
      "8511        Home     Alone   Sunny           80   6PM                    Bar   \n",
      "8512        Home   Partner   Sunny           30  10PM  Carry out & Take away   \n",
      "8513        Work     Alone   Rainy           55   7AM        Restaurant(<20)   \n",
      "8515        Work     Alone   Snowy           30   7AM      Restaurant(20-50)   \n",
      "8516        Work     Alone   Sunny           80   7AM        Restaurant(<20)   \n",
      "\n",
      "     expiration  gender age    maritalStatus  ...  CoffeeHouse CarryAway  \\\n",
      "4192         1d    Male  26           Single  ...        never       1~3   \n",
      "4236         1d    Male  26           Single  ...          gt8       gt8   \n",
      "4280         1d  Female  26           Single  ...        never       4~8   \n",
      "4324         1d  Female  46           Single  ...        never       4~8   \n",
      "4409         1d  Female  21           Single  ...        never     less1   \n",
      "...         ...     ...  ..              ...  ...          ...       ...   \n",
      "8511         2h    Male  46  Married partner  ...          1~3       1~3   \n",
      "8512         2h    Male  46  Married partner  ...          1~3       1~3   \n",
      "8513         2h    Male  46  Married partner  ...          1~3       1~3   \n",
      "8515         1d    Male  46  Married partner  ...          1~3       1~3   \n",
      "8516         1d    Male  46  Married partner  ...          1~3       1~3   \n",
      "\n",
      "     RestaurantLessThan20 Restaurant20To50 toCoupon_GEQ5min toCoupon_GEQ15min  \\\n",
      "4192                less1            less1                1                 1   \n",
      "4236                  4~8            less1                1                 1   \n",
      "4280                  1~3            less1                1                 1   \n",
      "4324                  1~3              1~3                1                 1   \n",
      "4409                  1~3            never                1                 1   \n",
      "...                   ...              ...              ...               ...   \n",
      "8511                less1              1~3                1                 0   \n",
      "8512                less1              1~3                1                 1   \n",
      "8513                less1              1~3                1                 1   \n",
      "8515                less1              1~3                1                 1   \n",
      "8516                less1              1~3                1                 0   \n",
      "\n",
      "     toCoupon_GEQ25min direction_same direction_opp  Y  \n",
      "4192                 1              0             1  1  \n",
      "4236                 1              0             1  1  \n",
      "4280                 1              0             1  1  \n",
      "4324                 1              0             1  1  \n",
      "4409                 1              0             1  0  \n",
      "...                ...            ...           ... ..  \n",
      "8511                 0              1             0  1  \n",
      "8512                 0              0             1  1  \n",
      "8513                 1              0             1  0  \n",
      "8515                 1              0             1  0  \n",
      "8516                 0              1             0  1  \n",
      "\n",
      "[74 rows x 26 columns]\n"
     ]
    }
   ],
   "source": [
    "# Check for duplicate rows\n",
    "duplicate_rows = data[data.duplicated()]\n",
    "\n",
    "print(\"Duplicate Rows:\")\n",
    "print(duplicate_rows)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given that there is no participant ID associated with each scenario, I will infer that the 74 duplicate rows likely represent the same scenario selected by multiple respondents. Consequently, I am opting not to remove these duplicate rows. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "destination                 0\n",
       "passanger                   0\n",
       "weather                     0\n",
       "temperature                 0\n",
       "time                        0\n",
       "coupon                      0\n",
       "expiration                  0\n",
       "gender                      0\n",
       "age                         0\n",
       "maritalStatus               0\n",
       "has_children                0\n",
       "education                   0\n",
       "occupation                  0\n",
       "income                      0\n",
       "car                     12576\n",
       "Bar                       107\n",
       "CoffeeHouse               217\n",
       "CarryAway                 151\n",
       "RestaurantLessThan20      130\n",
       "Restaurant20To50          189\n",
       "toCoupon_GEQ5min            0\n",
       "toCoupon_GEQ15min           0\n",
       "toCoupon_GEQ25min           0\n",
       "direction_same              0\n",
       "direction_opp               0\n",
       "Y                           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count null values\n",
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Scooter and motorcycle                      22\n",
       "Mazda5                                      22\n",
       "do not drive                                22\n",
       "crossover                                   21\n",
       "Car that is too old to install Onstar :D    21\n",
       "Name: car, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Investigatin car column values\n",
    "data['car'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>CoffeeHouse</th>\n",
       "      <th>CarryAway</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>517</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Male</td>\n",
       "      <td>50plus</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>518</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>1d</td>\n",
       "      <td>Male</td>\n",
       "      <td>50plus</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>519</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Restaurant(&lt;20)</td>\n",
       "      <td>1d</td>\n",
       "      <td>Male</td>\n",
       "      <td>50plus</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         destination  passanger weather  temperature  time           coupon  \\\n",
       "517  No Urgent Place  Friend(s)   Sunny           80  10AM              Bar   \n",
       "518  No Urgent Place  Friend(s)   Sunny           80   2PM     Coffee House   \n",
       "519  No Urgent Place  Friend(s)   Sunny           80   2PM  Restaurant(<20)   \n",
       "\n",
       "    expiration gender     age maritalStatus  ...  CoffeeHouse CarryAway  \\\n",
       "517         1d   Male  50plus      Divorced  ...          NaN       NaN   \n",
       "518         1d   Male  50plus      Divorced  ...          NaN       NaN   \n",
       "519         1d   Male  50plus      Divorced  ...          NaN       NaN   \n",
       "\n",
       "    RestaurantLessThan20 Restaurant20To50 toCoupon_GEQ5min toCoupon_GEQ15min  \\\n",
       "517                  NaN              NaN                1                 0   \n",
       "518                  NaN              NaN                1                 0   \n",
       "519                  NaN              NaN                1                 1   \n",
       "\n",
       "    toCoupon_GEQ25min direction_same direction_opp  Y  \n",
       "517                 0              0             1  0  \n",
       "518                 0              0             1  0  \n",
       "519                 0              0             1  1  \n",
       "\n",
       "[3 rows x 26 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Creating a data frame with missing values for the Bar column\n",
    "age_dist= data[data['Bar'].isnull()]\n",
    "age_dist.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "41        28\n",
       "31        27\n",
       "36        22\n",
       "50plus    12\n",
       "26        12\n",
       "21         6\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Checking which age group has most missing values in the \"Bar\" column. \n",
    "age_dist['age'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "less1    1648\n",
       "never    1628\n",
       "1~3       792\n",
       "4~8       241\n",
       "gt8        65\n",
       "Name: Bar, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filtering on top 3 age groups \n",
    "mid_life = data[(data['age'] == '41') | (data['age'] == '31') | (data['age'] == '36')]\n",
    "mid_life['Bar'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>CoffeeHouse</th>\n",
       "      <th>CarryAway</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>495</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Restaurant(&lt;20)</td>\n",
       "      <td>1d</td>\n",
       "      <td>Male</td>\n",
       "      <td>26</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>less1</td>\n",
       "      <td>less1</td>\n",
       "      <td>less1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>496</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>2h</td>\n",
       "      <td>Male</td>\n",
       "      <td>26</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>less1</td>\n",
       "      <td>less1</td>\n",
       "      <td>less1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Carry out &amp; Take away</td>\n",
       "      <td>2h</td>\n",
       "      <td>Male</td>\n",
       "      <td>26</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>less1</td>\n",
       "      <td>less1</td>\n",
       "      <td>less1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         destination  passanger weather  temperature  time  \\\n",
       "495  No Urgent Place      Alone   Sunny           55   2PM   \n",
       "496  No Urgent Place  Friend(s)   Sunny           80  10AM   \n",
       "497  No Urgent Place  Friend(s)   Sunny           80  10AM   \n",
       "\n",
       "                    coupon expiration gender age      maritalStatus  ...  \\\n",
       "495        Restaurant(<20)         1d   Male  26  Unmarried partner  ...   \n",
       "496           Coffee House         2h   Male  26  Unmarried partner  ...   \n",
       "497  Carry out & Take away         2h   Male  26  Unmarried partner  ...   \n",
       "\n",
       "     CoffeeHouse CarryAway RestaurantLessThan20 Restaurant20To50  \\\n",
       "495          NaN     less1                less1            less1   \n",
       "496          NaN     less1                less1            less1   \n",
       "497          NaN     less1                less1            less1   \n",
       "\n",
       "    toCoupon_GEQ5min toCoupon_GEQ15min toCoupon_GEQ25min direction_same  \\\n",
       "495                1                 0                 0              0   \n",
       "496                1                 0                 0              0   \n",
       "497                1                 1                 0              0   \n",
       "\n",
       "    direction_opp  Y  \n",
       "495             1  1  \n",
       "496             1  1  \n",
       "497             1  0  \n",
       "\n",
       "[3 rows x 26 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Creating a data frame with missing values for the Coffee House column\n",
    "CHdist= data[data['CoffeeHouse'].isnull()]\n",
    "CHdist.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "26        122\n",
       "36         44\n",
       "31         27\n",
       "50plus     12\n",
       "41          6\n",
       "21          6\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Checking which age group has most missing values in the \"Coffee House\" column. \n",
    "age_dist['age'].value_counts()\n",
    "CHdist['age'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1~3      717\n",
       "less1    700\n",
       "never    520\n",
       "gt8      346\n",
       "4~8      154\n",
       "Name: CoffeeHouse, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filtering on the age groups '26'\n",
    "age26=data[data['age'] == '26']\n",
    "age26['CoffeeHouse'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21         50\n",
       "50plus     34\n",
       "26         34\n",
       "below21    21\n",
       "41          6\n",
       "31          6\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Applying same analysis process for carry away\n",
    "\n",
    "CAway= data[data['CarryAway'].isnull()]\n",
    "CAway['age'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1~3      2284\n",
       "4~8      1604\n",
       "gt8       601\n",
       "less1     595\n",
       "never      44\n",
       "Name: CarryAway, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Looking up the most common answer for ages 21 & 26\n",
    "age21_26 = data[(data['age'] == '21') | (data['age'] == '26')]\n",
    "age21_26['CarryAway'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "31        50\n",
       "21        50\n",
       "50plus    12\n",
       "26        12\n",
       "41         6\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# looking up most frequent age groups for Restaurats Less than 20\n",
    "RLess20= data[data['RestaurantLessThan20'].isnull()]\n",
    "RLess20['age'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1~3      1838\n",
       "4~8      1490\n",
       "less1     747\n",
       "gt8       407\n",
       "never     110\n",
       "Name: RestaurantLessThan20, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filtering for seleted age groups to determine the most common answer\n",
    "rest21_31 = data[(data['age'] == '21') | (data['age'] == '31')]\n",
    "rest21_31['RestaurantLessThan20'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "31         49\n",
       "50plus     34\n",
       "26         28\n",
       "21         28\n",
       "below21    22\n",
       "46         22\n",
       "41          6\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Applying the same process to an expensive restaurant data\n",
    "\n",
    "R20_50= data[data['Restaurant20To50'].isnull()]\n",
    "R20_50['age'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "less1    2055\n",
       "1~3       893\n",
       "never     461\n",
       "4~8       242\n",
       "gt8        93\n",
       "Name: Restaurant20To50, dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filtering for age groups of interest\n",
    "\n",
    "rest31_50 = data[(data['age'] == '50plus') | (data['age'] == '31')]\n",
    "rest31_50['Restaurant20To50'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Decide what to do about your missing data -- drop, replace, other..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion\n",
    "\n",
    "Car: column has a high percentage of missing values and imputation or filling these missing values is not feasible or meaningful. Below are summary statistics for the Car column. \n",
    "\n",
    "Scooter and motorcycle                      22\n",
    "\n",
    "Mazda5                                      22\n",
    "\n",
    "do not drive                                22\n",
    "\n",
    "crossover                                   21\n",
    "\n",
    "Car that is too old to install Onstar :D    21\n",
    "\n",
    "\n",
    "Bar: To validate my imputation strategy, I analyzed the missing values segmented by the respondents' age group. The investigation revealed that the majority of the missing data pertained to ages between 31 and 41. Within this age bracket, the most frequent responses were \"never\" (n=1628) and \"less1\" (n=1648). Consequently, I selected \"less1\" as the replacement value for the null entries.\n",
    "\n",
    "I applied the same method to replace all other missing values.\n",
    "\n",
    "CoffeeHouse:1-3\n",
    "\n",
    "Carry away:1-3\n",
    "\n",
    "RestaurantLessThan20:1-3\n",
    "\n",
    "Restaurant20To50:less1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop the 'car' column\n",
    "data = data.drop('car', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['destination', 'passanger', 'weather', 'temperature', 'time', 'coupon', 'expiration', 'gender', 'age', 'maritalStatus', 'has_children', 'education', 'occupation', 'income', 'Bar', 'CoffeeHouse', 'CarryAway', 'RestaurantLessThan20', 'Restaurant20To50', 'toCoupon_GEQ5min', 'toCoupon_GEQ15min', 'toCoupon_GEQ25min', 'direction_same', 'direction_opp', 'Y']\n"
     ]
    }
   ],
   "source": [
    "# Doublechecking that the Car column has been dropped\n",
    "column_list = data.columns.tolist()\n",
    "print(column_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "never    5197\n",
       "less1    3589\n",
       "1~3      2473\n",
       "4~8      1076\n",
       "gt8       349\n",
       "Name: Bar, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Replacing all missing values with less1 in Bar column\n",
    "data['Bar'] = data['Bar'].fillna('less1')\n",
    "\n",
    "# Doublechecking that all missing values have been filled in\n",
    "data['Bar'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1~3      3442\n",
       "less1    3385\n",
       "never    2962\n",
       "4~8      1784\n",
       "gt8      1111\n",
       "Name: CoffeeHouse, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Replacing all missing values with 1-3 in CoffeeHouse column\n",
    "data['CoffeeHouse'] = data['CoffeeHouse'].fillna('1~3')\n",
    "\n",
    "# Doublechecking that all missing values have been filled in\n",
    "data['CoffeeHouse'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1~3      4823\n",
       "4~8      4258\n",
       "less1    1856\n",
       "gt8      1594\n",
       "never     153\n",
       "Name: CarryAway, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Replacing all missing values with 1-3 in CarryAway column\n",
    "data['CarryAway'] = data['CarryAway'].fillna('1~3')\n",
    "\n",
    "# Doublechecking that all missing values have been filled in\n",
    "data['CarryAway'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1~3      5506\n",
       "4~8      3580\n",
       "less1    2093\n",
       "gt8      1285\n",
       "never     220\n",
       "Name: RestaurantLessThan20, dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Replacing all missing values with 1-3 in RestaurantLessThan20 column\n",
    "data['RestaurantLessThan20'] = data['RestaurantLessThan20'].fillna('1~3')\n",
    "\n",
    "# Doublechecking that all missing values have been filled in\n",
    "data['RestaurantLessThan20'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "less1    6266\n",
       "1~3      3290\n",
       "never    2136\n",
       "4~8       728\n",
       "gt8       264\n",
       "Name: Restaurant20To50, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Replacing all missing values with 1-3 in Restaurant20To50 column\n",
    "data['Restaurant20To50'] = data['Restaurant20To50'].fillna('less1')\n",
    "\n",
    "# Doublechecking that all missing values have been filled in\n",
    "data['Restaurant20To50'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "destination             0\n",
       "passanger               0\n",
       "weather                 0\n",
       "temperature             0\n",
       "time                    0\n",
       "coupon                  0\n",
       "expiration              0\n",
       "gender                  0\n",
       "age                     0\n",
       "maritalStatus           0\n",
       "has_children            0\n",
       "education               0\n",
       "occupation              0\n",
       "income                  0\n",
       "Bar                     0\n",
       "CoffeeHouse             0\n",
       "CarryAway               0\n",
       "RestaurantLessThan20    0\n",
       "Restaurant20To50        0\n",
       "toCoupon_GEQ5min        0\n",
       "toCoupon_GEQ15min       0\n",
       "toCoupon_GEQ25min       0\n",
       "direction_same          0\n",
       "direction_opp           0\n",
       "Y                       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count null values again\n",
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. What proportion of the total observations chose to accept the coupon? \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    7210\n",
       "0    5474\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Getting counts for 1-accpted and 0-did not accept in the Y column\n",
    "data['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "56.8% of the total observations chose to accept the coupon."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Use a bar plot to visualize the `coupon` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>coupon</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Coffee House</td>\n",
       "      <td>3996</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Restaurant(&lt;20)</td>\n",
       "      <td>2786</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Carry out &amp; Take away</td>\n",
       "      <td>2393</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bar</td>\n",
       "      <td>2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Restaurant(20-50)</td>\n",
       "      <td>1492</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   index  coupon\n",
       "0           Coffee House    3996\n",
       "1        Restaurant(<20)    2786\n",
       "2  Carry out & Take away    2393\n",
       "3                    Bar    2017\n",
       "4      Restaurant(20-50)    1492"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Getting coupon count by the type of the coupon\n",
    "coupon_counts = data['coupon'].value_counts().reset_index()\n",
    "coupon_counts.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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NeYXL14cNjY2OHDggDItMTERAQEBcHFxAQA4OTlBX19fo01ERATOnz+vtHF2dkZMTAxOnz6ttDl16hRiYmKUNm8yNDSEmZmZxo2IiIhyr0wdPktJSYG+vn666fr6+khJSfng5fTv3x9r167F9u3bYWpqquwRUqvVMDY2hkqlgpeXF6ZMmYJSpUqhVKlSmDJlCvLly4cuXboobd3d3TFkyBAULFgQFhYWGDp0KMqXL6+cjVamTBk0adIEHh4eWLhwIYDXp+S7urqykzUREREByGQoqlevHgYNGoR169bBzs4OAHD//n389NNPqF+//gcvx8fHBwBQp04djenLly9H9+7dAQDDhg1DfHw8+vXrh+joaFSvXh379+9XxigCXl92RE9PDx07dkR8fDzq168PX19fZYwiAFizZg08PT2Vs9RatmwJb2/vzKw+ERER5UKZCkXe3t5o1aoVihUrBnt7e6hUKty5cwfly5fH6tWrP3g5IvLeNiqVCuPHj8f48ePf2sbIyAjz5s3DvHnz3trGwsLio2ojIiKivCVTocje3h5nzpzBgQMHcOnSJYgIypYtqxyuIiIiIsppPqqj9eHDh1G2bFllzJ6GDRti4MCB8PT0RNWqVVGuXDkcO3bssxRKRERE9Dl9VCiaPXs2PDw8MjwTS61Wo3fv3pg5c+YnK46IiIgoq3xUKPrnn3/QpEmTt85v1KgRQkND/3NRRERERFnto0LRgwcPMjwVP5Wenh4ePnz4n4siIiIiymofFYq++OILnDt37q3zz549C1tb2/9cFBEREVFW+6hQ1KxZM4wbNw4vX75MNy8+Ph6//PILXF1dP1lxRERERFnlo07JHzNmDLZs2YLSpUtjwIABcHBwgEqlQnh4OObPn4/k5GSMHj36c9VKRERE9Nl8VCiytrZGYGAg+vbti5EjRyqDL6pUKjRu3Bh//vnnWy+wSkRERJSdffTgjUWLFsWePXsQHR2Na9euQURQqlQpmJubf476iIiIiLJEpka0BgBzc3NUrVr1U9ZCREREpDUf1dGaiIiIKLdiKCIiIiICQxERERERAIYiIiIiIgAMRUREREQAGIqIiIiIADAUEREREQFgKCIiIiICwFBEREREBIChiIiIiAgAQxERERERAIYiIiIiIgAMRUREREQAGIqIiIiIADAUEREREQFgKCIiIiICwFBEREREBIChiIiIiAgAQxERERERAIYiIiIiIgAMRUREREQAGIqIiIiIAGg5FP31119o0aIF7OzsoFKpsG3bNo353bt3h0ql0rjVqFFDo01CQgIGDhwIS0tLmJiYoGXLlrh3755Gm+joaLi5uUGtVkOtVsPNzQ1Pnz79zGtHREREOYlWQ9Hz589RsWJFeHt7v7VNkyZNEBERodz27NmjMd/Lywtbt26Fn58fjh8/jri4OLi6uiI5OVlp06VLF4SFhcHf3x/+/v4ICwuDm5vbZ1svIiIiynn0tPnkTZs2RdOmTd/ZxtDQEDY2NhnOi4mJwdKlS7Fq1So0aNAAALB69WrY29vj4MGDaNy4McLDw+Hv74+TJ0+ievXqAIDFixfD2dkZly9fhoODw6ddKSIiIsqRsn2foqNHj8LKygqlS5eGh4cHoqKilHmhoaFISkpCo0aNlGl2dnZwdHREYGAgACAoKAhqtVoJRABQo0YNqNVqpQ0RERGRVvcUvU/Tpk3RoUMHFC1aFDdv3sTYsWNRr149hIaGwtDQEJGRkTAwMIC5ubnG46ytrREZGQkAiIyMhJWVVbplW1lZKW0ykpCQgISEBOV+bGzsJ1orIiIiyo6ydSjq1KmT8n9HR0dUqVIFRYsWxe7du9G2bdu3Pk5EoFKplPtp//+2Nm+aOnUqJkyYkMnKiYiI3s97yE5tl5CjDfijxSddXrY/fJaWra0tihYtiqtXrwIAbGxskJiYiOjoaI12UVFRsLa2Vto8ePAg3bIePnyotMnIyJEjERMTo9zu3r37CdeEiIiIspscFYoeP36Mu3fvwtbWFgDg5OQEfX19HDhwQGkTERGB8+fPw8XFBQDg7OyMmJgYnD59Wmlz6tQpxMTEKG0yYmhoCDMzM40bERER5V5aPXwWFxeHa9euKfdv3ryJsLAwWFhYwMLCAuPHj0e7du1ga2uLW7duYdSoUbC0tESbNm0AAGq1Gu7u7hgyZAgKFiwICwsLDB06FOXLl1fORitTpgyaNGkCDw8PLFy4EADQq1cvuLq68swzIiIiUmg1FIWEhKBu3brK/cGDBwMAunXrBh8fH5w7dw4rV67E06dPYWtri7p162L9+vUwNTVVHjNr1izo6emhY8eOiI+PR/369eHr6wtdXV2lzZo1a+Dp6amcpdayZct3jo1EREREeY9WQ1GdOnUgIm+dv2/fvvcuw8jICPPmzcO8efPe2sbCwgKrV6/OVI1ERESUN+SoPkVEREREnwtDEREREREYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERAAYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERAAYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERAAYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAFoORX/99RdatGgBOzs7qFQqbNu2TWO+iGD8+PGws7ODsbEx6tSpgwsXLmi0SUhIwMCBA2FpaQkTExO0bNkS9+7d02gTHR0NNzc3qNVqqNVquLm54enTp5957YiIiCgn0Wooev78OSpWrAhvb+8M50+fPh0zZ86Et7c3goODYWNjg4YNG+LZs2dKGy8vL2zduhV+fn44fvw44uLi4OrqiuTkZKVNly5dEBYWBn9/f/j7+yMsLAxubm6fff2IiIgo59DT5pM3bdoUTZs2zXCeiGD27NkYPXo02rZtCwBYsWIFrK2tsXbtWvTu3RsxMTFYunQpVq1ahQYNGgAAVq9eDXt7exw8eBCNGzdGeHg4/P39cfLkSVSvXh0AsHjxYjg7O+Py5ctwcHDImpUlIiKibC3b9im6efMmIiMj0ahRI2WaoaEhateujcDAQABAaGgokpKSNNrY2dnB0dFRaRMUFAS1Wq0EIgCoUaMG1Gq10oaIiIhIq3uK3iUyMhIAYG1trTHd2toat2/fVtoYGBjA3Nw8XZvUx0dGRsLKyird8q2srJQ2GUlISEBCQoJyPzY2NnMrQkRERDlCtt1TlEqlUmncF5F00970ZpuM2r9vOVOnTlU6ZqvVatjb239k5URERJSTZNtQZGNjAwDp9uZERUUpe49sbGyQmJiI6Ojod7Z58OBBuuU/fPgw3V6otEaOHImYmBjldvfu3f+0PkRERJS9ZdtQVLx4cdjY2ODAgQPKtMTERAQEBMDFxQUA4OTkBH19fY02EREROH/+vNLG2dkZMTExOH36tNLm1KlTiImJUdpkxNDQEGZmZho3IiIiyr202qcoLi4O165dU+7fvHkTYWFhsLCwQJEiReDl5YUpU6agVKlSKFWqFKZMmYJ8+fKhS5cuAAC1Wg13d3cMGTIEBQsWhIWFBYYOHYry5csrZ6OVKVMGTZo0gYeHBxYuXAgA6NWrF1xdXXnmGRERESm0GopCQkJQt25d5f7gwYMBAN26dYOvry+GDRuG+Ph49OvXD9HR0ahevTr2798PU1NT5TGzZs2Cnp4eOnbsiPj4eNSvXx++vr7Q1dVV2qxZswaenp7KWWotW7Z869hIRERElDdpNRTVqVMHIvLW+SqVCuPHj8f48ePf2sbIyAjz5s3DvHnz3trGwsICq1ev/i+lEhERUS6XbfsUEREREWUlhiIiIiIiMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERAAYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERAAYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERAAYioiIiIgAMBQRERERAWAoIiIiIgLAUEREREQEgKGIiIiICABDEREREREAhiIiIiIiAAxFRERERACyeSgaP348VCqVxs3GxkaZLyIYP3487OzsYGxsjDp16uDChQsay0hISMDAgQNhaWkJExMTtGzZEvfu3cvqVSEiIqJsLluHIgAoV64cIiIilNu5c+eUedOnT8fMmTPh7e2N4OBg2NjYoGHDhnj27JnSxsvLC1u3boWfnx+OHz+OuLg4uLq6Ijk5WRurQ0RERNmUnrYLeB89PT2NvUOpRASzZ8/G6NGj0bZtWwDAihUrYG1tjbVr16J3796IiYnB0qVLsWrVKjRo0AAAsHr1atjb2+PgwYNo3Lhxlq4LERERZV/Zfk/R1atXYWdnh+LFi6Nz5864ceMGAODmzZuIjIxEo0aNlLaGhoaoXbs2AgMDAQChoaFISkrSaGNnZwdHR0elDRERERGQzfcUVa9eHStXrkTp0qXx4MEDTJ48GS4uLrhw4QIiIyMBANbW1hqPsba2xu3btwEAkZGRMDAwgLm5ebo2qY9/m4SEBCQkJCj3Y2NjP8UqERERUTaVrUNR06ZNlf+XL18ezs7O+PLLL7FixQrUqFEDAKBSqTQeIyLppr3pQ9pMnToVEyZMyGTlRERElNNk+8NnaZmYmKB8+fK4evWq0s/ozT0+UVFRyt4jGxsbJCYmIjo6+q1t3mbkyJGIiYlRbnfv3v2Ea0JERETZTY4KRQkJCQgPD4etrS2KFy8OGxsbHDhwQJmfmJiIgIAAuLi4AACcnJygr6+v0SYiIgLnz59X2ryNoaEhzMzMNG5ERESUe2Xrw2dDhw5FixYtUKRIEURFRWHy5MmIjY1Ft27doFKp4OXlhSlTpqBUqVIoVaoUpkyZgnz58qFLly4AALVaDXd3dwwZMgQFCxaEhYUFhg4divLlyytnoxEREREB2TwU3bt3D9999x0ePXqEQoUKoUaNGjh58iSKFi0KABg2bBji4+PRr18/REdHo3r16ti/fz9MTU2VZcyaNQt6enro2LEj4uPjUb9+ffj6+kJXV1dbq0VERETZULYORX5+fu+cr1KpMH78eIwfP/6tbYyMjDBv3jzMmzfvE1dHREREuUmO6lNERERE9LkwFBERERGBoYiIiIgIAEMREREREQCGIiIiIiIADEVEREREABiKiIiIiAAwFBEREREBYCgiIiIiAsBQRERERASAoYiIiIgIAEMREREREQCGIiIiIiIADEVEREREABiKiIiIiAAwFBEREREBYCgiIiIiAsBQRERERASAoYiIiIgIAEMREREREQCGIiIiIiIADEVEREREABiKiIiIiAAwFBEREREBYCgiIiIiAsBQRERERASAoYiIiIgIAEMREREREQCGIiIiIiIADEVEREREABiKiIiIiAAwFBEREREBYCgiIiIiApDHQtGff/6J4sWLw8jICE5OTjh27Ji2SyIiIqJsIs+EovXr18PLywujR4/G33//jW+++QZNmzbFnTt3tF0aERERZQN5JhTNnDkT7u7u+PHHH1GmTBnMnj0b9vb28PHx0XZpRERElA3kiVCUmJiI0NBQNGrUSGN6o0aNEBgYqKWqiIiIKDvR03YBWeHRo0dITk6GtbW1xnRra2tERkZm+JiEhAQkJCQo92NiYgAAsbGx732+5IT4/1Bt3vYhr+/HePYy+ZMuLy/51O/Fq/hXn3R5ecmnfi+ev+J78V98yvcjPuHFJ1tWXvQh70VqGxF5b9s8EYpSqVQqjfsikm5aqqlTp2LChAnpptvb23+W2ug19bw+2i6BUk1Va7sC+h/1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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Creating a bar plot\n",
    "sns.barplot(x='index',y='coupon', data=coupon_counts)\n",
    "\n",
    "# Add labels and title\n",
    "plt.xlabel('Coupon Type')\n",
    "plt.ylabel('Counts')\n",
    "plt.title('Coupon Counts by Coupon Type')\n",
    "plt.xticks(rotation=45)\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Use a histogram to visualize the temperature column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>temperature</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>80</td>\n",
       "      <td>6528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>3840</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>30</td>\n",
       "      <td>2316</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index  temperature\n",
       "0     80         6528\n",
       "1     55         3840\n",
       "2     30         2316"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['temperature'].value_counts().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAeoAAAH+CAYAAABTKk23AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABdIklEQVR4nO3de1gU9f4H8PfCwnIRVu4LCoqKiIL3Qugi5V3JysoMJT2ZespUKn+VeUoqQ7NSS9PMTC01u6l5zEjNS5moiAcVRNREAeWmwnJfYPf7+wOZXMALiOwA79fz7JM789mdzwwbb2bmuzMKIYQAERERyZKZqRsgIiKiG2NQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQU6NRKBS39di7d6+pWzWZ7du3IzIy0tRt1GrNmjVGPycrKytoNBo89NBDmDdvHrKzs2u8JjIyEgqFok7LKS4uRmRkZJ0/B7Utq3379ggNDa3T+9zKhg0bsHjx4lrnKRQKk/z8qv9slEol2rZti3/961+4ePGiVLd37956/z924MABREZGIi8vr+Eap9uiNHUD1HLExMQYPX/vvfewZ88e7N6922h6165dG7MtWdm+fTs+++wz2YY1AKxevRpdunRBeXk5srOzsX//fnzwwQf46KOP8N1332HgwIFS7fPPP4+hQ4fW6f2Li4vxzjvvAABCQkJu+3X1WVZ9bNiwAQkJCYiIiKgxLyYmBm3btr3rPdxI1c+mpKQEf/zxB+bNm4d9+/bhxIkTsLW1vaP3PnDgAN555x1MmDABrVu3bpiG6bYwqKnR9OvXz+i5i4sLzMzMakxvToqLi2FjY2PqNhq0D39/f/Tt21d6/sQTT+Dll1/G/fffj1GjRuHMmTNwc3MDALRt2/auB1fVujXGsm7F1J/l6382Dz30EPR6Pd577z1s2bIFY8eONWlvVH889E2yUlZWhrlz56JLly5QqVRwcXHBv/71L+Tk5BjVVR3S3LZtG3r16gVra2v4+flh27ZtACoPBfr5+cHW1hb33nsvjhw5YvT6CRMmoFWrVkhMTMSAAQNga2sLFxcXvPTSSyguLjaqFUJg2bJl6NmzJ6ytreHg4IAnn3wS586dM6oLCQmBv78//vjjDwQHB8PGxgbPPfccAOC7777D4MGD4e7uLvX6xhtvoKioyKinzz77DIDxaYLz58/j/PnzUCgUWLNmTY1tVv1wa9Uh4KNHj+LJJ5+Eg4MDOnbsWKd1qSsvLy98/PHHKCgowIoVK2r0cr3du3cjJCQETk5OsLa2hpeXF5544gkUFxfj/PnzcHFxAQC888470jaYMGHCLdftZofZN2/ejO7du8PKygodOnTAp59+ajS/6tDx+fPnjaZXP1QcEhKCX375BRcuXDD6GVWp7dB3QkICHn30UTg4OMDKygo9e/bE2rVra13Ot99+i9mzZ8PDwwP29vYYOHAgkpOTb7zhb6HqD4cLFy7ctG7r1q0ICgqCjY0N7OzsMGjQIKMjYJGRkfi///s/AIC3tzdPUzUyBjXJhsFgwKOPPor58+cjLCwMv/zyC+bPn4+dO3ciJCQEJSUlRvXHjh3DrFmz8Prrr2PTpk1Qq9UYNWoU5syZgy+//BJRUVFYv349tFotQkNDa7y+vLwcw4cPx4ABA7Blyxa89NJLWLFiBZ5++mmjuilTpiAiIgIDBw7Eli1bsGzZMiQmJiI4OBhZWVlGtRkZGRg3bhzCwsKwfft2vPjiiwCAM2fOYPjw4Vi1ahWio6MRERGB77//Ho888oj02rfeegtPPvkkgMpDqFUPd3f3em3PUaNGoVOnTvjhhx/w+eef13ld6mr48OEwNzfHH3/8ccOa8+fPY8SIEbC0tMRXX32F6OhozJ8/H7a2tigrK4O7uzuio6MBABMnTpS2wVtvvXXLdbuR+Ph4RERE4OWXX8bmzZsRHByMGTNm4KOPPqrzOi5btgz33XcfNBqN0c/oRpKTkxEcHIzExER8+umn2LRpE7p27YoJEyZgwYIFNerffPNNXLhwAV9++SW++OILnDlzBo888gj0en2dewWAs2fPAoD0x09tNmzYgEcffRT29vb49ttvsWrVKuTm5iIkJAT79+8HUHlaYdq0aQCATZs2Sevdu3fvevVFdSSITGT8+PHC1tZWev7tt98KAOKnn34yqouNjRUAxLJly6Rp7dq1E9bW1iI9PV2aFh8fLwAId3d3UVRUJE3fsmWLACC2bt1qtGwA4pNPPjFa1vvvvy8AiP379wshhIiJiREAxMcff2xUl5aWJqytrcVrr70mTevfv78AIH7//febrrfBYBDl5eVi3759AoA4duyYNG/q1Kmitv8tU1JSBACxevXqGvMAiDlz5kjP58yZIwCIt99+26iuLutSm9WrVwsAIjY29oY1bm5uws/Pr0YvVX788UcBQMTHx9/wPXJycmqs063WrbZlCVH5OVEoFDWWN2jQIGFvby99TqrWLSUlxahuz549AoDYs2ePNG3EiBGiXbt2tfZeve8xY8YIlUolUlNTjeqGDRsmbGxsRF5entFyhg8fblT3/fffCwAiJiam1uVVqer/4MGDory8XBQUFIht27YJFxcXYWdnJzIzM2tdH71eLzw8PERAQIDQ6/XS+xUUFAhXV1cRHBwsTfvwww9r3UZ093GPmmRj27ZtaN26NR555BFUVFRIj549e0Kj0dQ4zNazZ0+0adNGeu7n5weg8vDk9edjq6bXdviv+nm7sLAwAMCePXuknhQKBcaNG2fUk0ajQY8ePWr05ODggIcffrjGcs6dO4ewsDBoNBqYm5vDwsIC/fv3BwAkJSXdzuapsyeeeMLoeV3XpT7ELW5v37NnT1haWmLy5MlYu3ZtvQ+5V1+3m+nWrRt69OhhNC0sLAz5+fk4evRovZZ/u3bv3o0BAwbA09PTaPqECRNQXFxcY2985MiRRs+7d+8O4NaHrqv069cPFhYWsLOzQ2hoKDQaDX799VdpzEB1ycnJuHTpEsLDw2Fm9k8ctGrVCk888QQOHjxY41QQNT4OJiPZyMrKQl5eHiwtLWudf/nyZaPnjo6ORs+rXnej6aWlpUbTlUolnJycjKZpNBoAwJUrV6SehBA3/EXXoUMHo+e1HaYuLCzEAw88ACsrK8ydOxedO3eGjY0N0tLSMGrUqBqH5BtK9V7qui51VVRUhCtXriAgIOCGNR07dsSuXbuwYMECTJ06FUVFRejQoQOmT5+OGTNm3Pay6nI6oOpnWtu0qp/z3XLlypVae/Xw8Kh1+dU/jyqVCgBu+zPy9ddfw8/PD0qlEm5ubrfcTlXLv1GPBoMBubm5shgQ2ZIxqEk2nJ2d4eTkJJ2jrM7Ozq5Bl1dRUYErV64Y/XLMzMwE8M8vTGdnZygUCvz555/SL83rVZ9W22Cm3bt349KlS9i7d6+0Fw2gTt9HtbKyAgDodDqj6TcLmuq91HVd6uqXX36BXq+/5VeqHnjgATzwwAPQ6/U4cuQIlixZgoiICLi5uWHMmDG3tay6fDe76mda27Sqn/ONtm/1Pw7rysnJCRkZGTWmX7p0CUDlz6Qh+fn5GY3Iv5Wq9b9Rj2ZmZnBwcGiw/qh+eOibZCM0NBRXrlyBXq9H3759azx8fX0bfJnr1683er5hwwYA/3x/NzQ0FEIIXLx4sdaebrb3WKUqVKoH4fWjo6vcaA/Kzc0NVlZWOH78uNH0n3/++ZbLr9IQ63IjqampmDlzJtRqNaZMmXJbrzE3N0dgYKA00r3qMHRd9yJvJTExEceOHTOatmHDBtjZ2UmDodq3bw8ANbbv1q1ba7yfSqW67d4GDBgg/aF2va+//ho2NjYm/zqXr68v2rRpgw0bNhidtigqKsJPP/0kjQQHGv7nQrePe9QkG2PGjMH69esxfPhwzJgxA/feey8sLCyQnp6OPXv24NFHH8Xjjz/eYMuztLTExx9/jMLCQtxzzz04cOAA5s6di2HDhuH+++8HANx3332YPHky/vWvf+HIkSN48MEHYWtri4yMDOzfvx8BAQF44YUXbrqc4OBgODg44N///jfmzJkDCwsLrF+/vkZ4AJDC8oMPPsCwYcNgbm6O7t27w9LSEuPGjcNXX32Fjh07okePHjh8+LD0h8XtaIh1ASq/blR1fjs7Oxt//vknVq9eDXNzc2zevPmmI4w///xz7N69GyNGjICXlxdKS0vx1VdfAYB0oRQ7Ozu0a9cOP//8MwYMGABHR0c4OztLYVpXHh4eGDlyJCIjI+Hu7o5169Zh586d+OCDD6QQuueee+Dr64uZM2eioqICDg4O2Lx5szTq+XoBAQHYtGkTli9fjj59+sDMzOyGe7Fz5szBtm3b8NBDD+Htt9+Go6Mj1q9fj19++QULFiyAWq2u1zo1FDMzMyxYsABjx45FaGgopkyZAp1Ohw8//BB5eXmYP3++VFv12fzkk08wfvx4WFhYwNfXt8GPdFEtTDmSjVq26qO+hRCivLxcfPTRR6JHjx7CyspKtGrVSnTp0kVMmTJFnDlzRqpr166dGDFiRI33BCCmTp1qNK1qxPSHH35YY9nHjx8XISEhwtraWjg6OooXXnhBFBYW1njfr776SgQGBgpbW1thbW0tOnbsKJ599llx5MgRqaZ///6iW7duta7rgQMHRFBQkLCxsREuLi7i+eefF0ePHq0xklun04nnn39euLi4CIVCYTTKVqvViueff164ubkJW1tb8cgjj4jz58/fcNR3Tk5Orb3czrrUpmpkcdXD0tJSuLq6iv79+4uoqCiRnZ1d4zXVR2LHxMSIxx9/XLRr106oVCrh5OQk+vfvbzQiXwghdu3aJXr16iVUKpUAIMaPH3/LdbvRqO8RI0aIH3/8UXTr1k1YWlqK9u3bi4ULF9Z4/enTp8XgwYOFvb29cHFxEdOmTRO//PJLjVHfV69eFU8++aRo3bq19DOqUv1nIYQQJ06cEI888ohQq9XC0tJS9OjRo8bo/arR2D/88IPR9JuN9r/e7YzIv34516+PEJXfjAgMDBRWVlbC1tZWDBgwQPz11181Xj9r1izh4eEhzMzMan0fujsUQtximCZRMzRhwgT8+OOPKCwsNHUrREQ3xXPUREREMsagJiIikjEe+iYiIpIx7lETERHJGIOaiIhIxhjUREREMsagvk1CCOTn59/ypgNEREQNiUF9mwoKCqBWq1FQUGDqVoiIqAVhUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZMykQd2+fXsoFIoaj6lTpwKo/O5yZGQkPDw8YG1tjZCQECQmJhq9h06nw7Rp0+Ds7AxbW1uMHDkS6enpRjW5ubkIDw+HWq2GWq1GeHg48vLyGms1iYiI6s2kQR0bG4uMjAzpsXPnTgDAU089BQBYsGABFi5ciKVLlyI2NhYajQaDBg0y+i5zREQENm/ejI0bN2L//v0oLCxEaGgo9Hq9VBMWFob4+HhER0cjOjoa8fHxCA8Pb9yVJSIiqg8hIzNmzBAdO3YUBoNBGAwGodFoxPz586X5paWlQq1Wi88//1wIIUReXp6wsLAQGzdulGouXrwozMzMRHR0tBBCiJMnTwoA4uDBg1JNTEyMACBOnTp1271ptVoBQGi12jtdTSIiotsmm3PUZWVlWLduHZ577jkoFAqkpKQgMzMTgwcPlmpUKhX69++PAwcOAADi4uJQXl5uVOPh4QF/f3+pJiYmBmq1GoGBgVJNv379oFarpZra6HQ65OfnGz2IiIgam2yCesuWLcjLy8OECRMAAJmZmQAANzc3ozo3NzdpXmZmJiwtLeHg4HDTGldX1xrLc3V1lWpqM2/ePOmctlqthqenZ73XjYiIqL5kE9SrVq3CsGHD4OHhYTRdoVAYPRdC1JhWXfWa2upv9T6zZs2CVquVHmlpabezGkRERA1KFkF94cIF7Nq1C88//7w0TaPRAECNvd7s7GxpL1uj0aCsrAy5ubk3rcnKyqqxzJycnBp769dTqVSwt7c3ehARETU2WQT16tWr4erqihEjRkjTvL29odFopJHgQOV57H379iE4OBgA0KdPH1hYWBjVZGRkICEhQaoJCgqCVqvF4cOHpZpDhw5Bq9VKNURERHKlNHUDBoMBq1evxvjx46FU/tOOQqFAREQEoqKi4OPjAx8fH0RFRcHGxgZhYWEAALVajYkTJ+LVV1+Fk5MTHB0dMXPmTAQEBGDgwIEAAD8/PwwdOhSTJk3CihUrAACTJ09GaGgofH19G3+FiYiI6sDkQb1r1y6kpqbiueeeqzHvtddeQ0lJCV588UXk5uYiMDAQO3bsgJ2dnVSzaNEiKJVKjB49GiUlJRgwYADWrFkDc3NzqWb9+vWYPn26NDp85MiRWLp06d1fOSIiojukEEIIUzfRFOTn50OtVkOr1fJ8NRERNRpZnKMmIiKi2jGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhlTmroBIiKixpSamorLly/X+/XOzs7w8vJqwI5ujkFNREQtRmpqKrr4+aGkuLje72FtY4NTSUmNFtYMaiIiajEuX76MkuJijH39Q7h5dazz67NS/8b6D/4Ply9fZlATERHdLW5eHdHWp5up27gtHExGREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkzORBffHiRYwbNw5OTk6wsbFBz549ERcXJ80XQiAyMhIeHh6wtrZGSEgIEhMTjd5Dp9Nh2rRpcHZ2hq2tLUaOHIn09HSjmtzcXISHh0OtVkOtViM8PBx5eXmNsYpERET1ZtKgzs3NxX333QcLCwv8+uuvOHnyJD7++GO0bt1aqlmwYAEWLlyIpUuXIjY2FhqNBoMGDUJBQYFUExERgc2bN2Pjxo3Yv38/CgsLERoaCr1eL9WEhYUhPj4e0dHRiI6ORnx8PMLDwxtzdYmIiOpMacqFf/DBB/D09MTq1aulae3bt5f+LYTA4sWLMXv2bIwaNQoAsHbtWri5uWHDhg2YMmUKtFotVq1ahW+++QYDBw4EAKxbtw6enp7YtWsXhgwZgqSkJERHR+PgwYMIDAwEAKxcuRJBQUFITk6Gr69v4600ERFRHZh0j3rr1q3o27cvnnrqKbi6uqJXr15YuXKlND8lJQWZmZkYPHiwNE2lUqF///44cOAAACAuLg7l5eVGNR4eHvD395dqYmJioFarpZAGgH79+kGtVks11el0OuTn5xs9iIiIGptJg/rcuXNYvnw5fHx88Ntvv+Hf//43pk+fjq+//hoAkJmZCQBwc3Mzep2bm5s0LzMzE5aWlnBwcLhpjaura43lu7q6SjXVzZs3TzqfrVar4enpeWcrS0REVA8mDWqDwYDevXsjKioKvXr1wpQpUzBp0iQsX77cqE6hUBg9F0LUmFZd9Zra6m/2PrNmzYJWq5UeaWlpt7taREREDcakQe3u7o6uXbsaTfPz80NqaioAQKPRAECNvd7s7GxpL1uj0aCsrAy5ubk3rcnKyqqx/JycnBp761VUKhXs7e2NHkRERI3NpEF93333ITk52Wja6dOn0a5dOwCAt7c3NBoNdu7cKc0vKyvDvn37EBwcDADo06cPLCwsjGoyMjKQkJAg1QQFBUGr1eLw4cNSzaFDh6DVaqUaIiIiOTLpqO+XX34ZwcHBiIqKwujRo3H48GF88cUX+OKLLwBUHq6OiIhAVFQUfHx84OPjg6ioKNjY2CAsLAwAoFarMXHiRLz66qtwcnKCo6MjZs6ciYCAAGkUuJ+fH4YOHYpJkyZhxYoVAIDJkycjNDSUI76JiEjWTBrU99xzDzZv3oxZs2bh3Xffhbe3NxYvXoyxY8dKNa+99hpKSkrw4osvIjc3F4GBgdixYwfs7OykmkWLFkGpVGL06NEoKSnBgAEDsGbNGpibm0s169evx/Tp06XR4SNHjsTSpUsbb2WJiIjqQSGEEKZuoinIz8+HWq2GVqvl+Woioibq6NGj6NOnD175bBPa+nSr8+vTzyRi4dRRiIuLQ+/eve9ChzWZ/BKiREREdGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiYiIZMykQR0ZGQmFQmH00Gg00nwhBCIjI+Hh4QFra2uEhIQgMTHR6D10Oh2mTZsGZ2dn2NraYuTIkUhPTzeqyc3NRXh4ONRqNdRqNcLDw5GXl9cYq0hERHRHTL5H3a1bN2RkZEiPEydOSPMWLFiAhQsXYunSpYiNjYVGo8GgQYNQUFAg1URERGDz5s3YuHEj9u/fj8LCQoSGhkKv10s1YWFhiI+PR3R0NKKjoxEfH4/w8PBGXU8iIqL6UJq8AaXSaC+6ihACixcvxuzZszFq1CgAwNq1a+Hm5oYNGzZgypQp0Gq1WLVqFb755hsMHDgQALBu3Tp4enpi165dGDJkCJKSkhAdHY2DBw8iMDAQALBy5UoEBQUhOTkZvr6+jbeyREREdWTyPeozZ87Aw8MD3t7eGDNmDM6dOwcASElJQWZmJgYPHizVqlQq9O/fHwcOHAAAxMXFoby83KjGw8MD/v7+Uk1MTAzUarUU0gDQr18/qNVqqYaIiEiuTLpHHRgYiK+//hqdO3dGVlYW5s6di+DgYCQmJiIzMxMA4ObmZvQaNzc3XLhwAQCQmZkJS0tLODg41Kipen1mZiZcXV1rLNvV1VWqqY1Op4NOp5Oe5+fn128liYiI7oBJg3rYsGHSvwMCAhAUFISOHTti7dq16NevHwBAoVAYvUYIUWNaddVraqu/1fvMmzcP77zzzm2tBxER0d1i8kPf17O1tUVAQADOnDkjnbeuvtebnZ0t7WVrNBqUlZUhNzf3pjVZWVk1lpWTk1Njb/16s2bNglarlR5paWl3tG5ERET1Iaug1ul0SEpKgru7O7y9vaHRaLBz505pfllZGfbt24fg4GAAQJ8+fWBhYWFUk5GRgYSEBKkmKCgIWq0Whw8flmoOHToErVYr1dRGpVLB3t7e6EFERNTYTHroe+bMmXjkkUfg5eWF7OxszJ07F/n5+Rg/fjwUCgUiIiIQFRUFHx8f+Pj4ICoqCjY2NggLCwMAqNVqTJw4Ea+++iqcnJzg6OiImTNnIiAgQBoF7ufnh6FDh2LSpElYsWIFAGDy5MkIDQ3liG8iIpI9kwZ1eno6nnnmGVy+fBkuLi7o168fDh48iHbt2gEAXnvtNZSUlODFF19Ebm4uAgMDsWPHDtjZ2UnvsWjRIiiVSowePRolJSUYMGAA1qxZA3Nzc6lm/fr1mD59ujQ6fOTIkVi6dGnjriwREVE9KIQQwtRNNAX5+flQq9XQarU8DE5E1EQdPXoUffr0wSufbUJbn251fn36mUQsnDoKcXFx6N27913osCZZnaMmIiIiYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkY7IJ6nnz5kGhUCAiIkKaJoRAZGQkPDw8YG1tjZCQECQmJhq9TqfTYdq0aXB2doatrS1GjhyJ9PR0o5rc3FyEh4dDrVZDrVYjPDwceXl5jbBWREREd0YWQR0bG4svvvgC3bt3N5q+YMECLFy4EEuXLkVsbCw0Gg0GDRqEgoICqSYiIgKbN2/Gxo0bsX//fhQWFiI0NBR6vV6qCQsLQ3x8PKKjoxEdHY34+HiEh4c32voRERHVl8mDurCwEGPHjsXKlSvh4OAgTRdCYPHixZg9ezZGjRoFf39/rF27FsXFxdiwYQMAQKvVYtWqVfj4448xcOBA9OrVC+vWrcOJEyewa9cuAEBSUhKio6Px5ZdfIigoCEFBQVi5ciW2bduG5ORkk6wzERHR7TJ5UE+dOhUjRozAwIEDjaanpKQgMzMTgwcPlqapVCr0798fBw4cAADExcWhvLzcqMbDwwP+/v5STUxMDNRqNQIDA6Wafv36Qa1WSzW10el0yM/PN3oQERE1NqUpF75x40bExcXhyJEjNeZlZmYCANzc3Iymu7m54cKFC1KNpaWl0Z54VU3V6zMzM+Hq6lrj/V1dXaWa2sybNw/vvPNO3VaIiIiogZlsjzotLQ0zZszA+vXrYWVldcM6hUJh9FwIUWNaddVraqu/1fvMmjULWq1WeqSlpd10mURERHeDyYI6Li4O2dnZ6NOnD5RKJZRKJfbt24dPP/0USqVS2pOuvtebnZ0tzdNoNCgrK0Nubu5Na7KysmosPycnp8be+vVUKhXs7e2NHkRERI2tXkF99OhRnDhxQnr+888/47HHHsObb76JsrKy23qPAQMG4MSJE4iPj5ceffv2xdixYxEfH48OHTpAo9Fg586d0mvKysqwb98+BAcHAwD69OkDCwsLo5qMjAwkJCRINUFBQdBqtTh8+LBUc+jQIWi1WqmGiIhIrup1jnrKlCl44403EBAQgHPnzmHMmDF4/PHH8cMPP6C4uBiLFy++5XvY2dnB39/faJqtrS2cnJyk6REREYiKioKPjw98fHwQFRUFGxsbhIWFAQDUajUmTpyIV199FU5OTnB0dMTMmTMREBAgDU7z8/PD0KFDMWnSJKxYsQIAMHnyZISGhsLX17c+q09ERNRo6hXUp0+fRs+ePQEAP/zwAx588EFs2LABf/31F8aMGXNbQX07XnvtNZSUlODFF19Ebm4uAgMDsWPHDtjZ2Uk1ixYtglKpxOjRo1FSUoIBAwZgzZo1MDc3l2rWr1+P6dOnS6PDR44ciaVLlzZIj0RERHdTvYJaCAGDwQAA2LVrF0JDQwEAnp6euHz5cr2b2bt3r9FzhUKByMhIREZG3vA1VlZWWLJkCZYsWXLDGkdHR6xbt67efREREZlKvc5R9+3bF3PnzsU333yDffv2YcSIEQAqv/t8swFaREREVDf1CupFixbh6NGjeOmllzB79mx06tQJAPDjjz9ygBYREVEDqteh7x49ehiN+q7y4YcfQqk06TVUiMjEUlNT7+gUmLOzM7y8vBqwI6KmrV6p2qFDB8TGxsLJycloemlpKXr37o1z5841SHNE1LSkpqaii58fSoqL6/0e1jY2OJWUxLAmuqZeQX3+/Hmju1NV0el0NW4xSUQtx+XLl1FSXIyxr38IN6+OdX59VurfWP/B/+Hy5csMaqJr6hTUW7dulf7922+/Qa1WS8/1ej1+//13eHt7N1x3RNQkuXl1RFufbqZug6hZqFNQP/bYYwAqvzY1fvx4o3kWFhZo3749Pv744wZrjoiIqKWrU1BXfXfa29sbsbGxcHZ2vitNERERUaV6naNOSUlp6D6IiIioFvX+LtXvv/+O33//HdnZ2dKedpWvvvrqjhsjIiKiegb1O++8g3fffRd9+/aFu7v7Le8PTURERPVTr6D+/PPPsWbNGoSHhzd0P0RERHSdel1CtKysjJcKJSIiagT1Curnn38eGzZsaOheiIiIqJp6HfouLS3FF198gV27dqF79+6wsLAwmr9w4cIGaY6IiKilq1dQHz9+HD179gQAJCQkGM3jwDIiIqKGU6+g3rNnT0P3QURERLWo1zlqIiIiahz12qN+6KGHbnqIe/fu3fVuiIiIiP5Rr6CuOj9dpby8HPHx8UhISKhxsw4iIiKqv3oF9aJFi2qdHhkZicLCwjtqiIiIiP7RoOeox40bx+t8ExERNaAGDeqYmBhYWVk15FsSERG1aPU69D1q1Cij50IIZGRk4MiRI3jrrbcapDEiIiKqZ1Cr1Wqj52ZmZvD19cW7776LwYMHN0hjREREVM+gXr16dUP3QURERLWoV1BXiYuLQ1JSEhQKBbp27YpevXo1VF9ERESEegZ1dnY2xowZg71796J169YQQkCr1eKhhx7Cxo0b4eLi0tB9EhERtUj1GvU9bdo05OfnIzExEVevXkVubi4SEhKQn5+P6dOnN3SPRERELVa99qijo6Oxa9cu+Pn5SdO6du2Kzz77jIPJiIiIGlC99qgNBkONe1ADgIWFBQwGwx03RURERJXqFdQPP/wwZsyYgUuXLknTLl68iJdffhkDBgxosOaIiIhaunoF9dKlS1FQUID27dujY8eO6NSpE7y9vVFQUIAlS5Y0dI9EREQtVr3OUXt6euLo0aPYuXMnTp06BSEEunbtioEDBzZ0f0RERC1anfaod+/eja5duyI/Px8AMGjQIEybNg3Tp0/HPffcg27duuHPP/+8K40SERG1RHUK6sWLF2PSpEmwt7evMU+tVmPKlClYuHBhgzVHRETU0tUpqI8dO4ahQ4fecP7gwYMRFxd3x00RERFRpToFdVZWVq1fy6qiVCqRk5Nzx00RERFRpToFdZs2bXDixIkbzj9+/Djc3d3vuCkiIiKqVKegHj58ON5++22UlpbWmFdSUoI5c+YgNDS0wZojIiJq6er09az//Oc/2LRpEzp37oyXXnoJvr6+UCgUSEpKwmeffQa9Xo/Zs2ffrV6JiIhanDoFtZubGw4cOIAXXngBs2bNghACAKBQKDBkyBAsW7YMbm5ud6VRIiKilqjOFzxp164dtm/fjtzcXJw9exZCCPj4+MDBweFu9EdERNSi1evKZADg4OCAe+65pyF7ISIiomrqda1vIiIiahwMaiIiIhljUBMREckYg5qIiEjGTBrUy5cvR/fu3WFvbw97e3sEBQXh119/leYLIRAZGQkPDw9YW1sjJCQEiYmJRu+h0+kwbdo0ODs7w9bWFiNHjkR6erpRTW5uLsLDw6FWq6FWqxEeHo68vLzGWEUiIqI7YtKgbtu2LebPn48jR47gyJEjePjhh/Hoo49KYbxgwQIsXLgQS5cuRWxsLDQaDQYNGoSCggLpPSIiIrB582Zs3LgR+/fvR2FhIUJDQ6HX66WasLAwxMfHIzo6GtHR0YiPj0d4eHijry8REVFd1fvrWQ3hkUceMXr+/vvvY/ny5Th48CC6du2KxYsXY/bs2Rg1ahQAYO3atXBzc8OGDRswZcoUaLVarFq1Ct988w0GDhwIAFi3bh08PT2xa9cuDBkyBElJSYiOjsbBgwcRGBgIAFi5ciWCgoKQnJwMX1/fxl1pIiKiOpDNOWq9Xo+NGzeiqKgIQUFBSElJQWZmJgYPHizVqFQq9O/fHwcOHAAAxMXFoby83KjGw8MD/v7+Uk1MTAzUarUU0gDQr18/qNVqqaY2Op0O+fn5Rg8iIqLGZvKgPnHiBFq1agWVSoV///vf2Lx5M7p27YrMzEwAqHFJUjc3N2leZmYmLC0ta1wVrXqNq6trjeW6urpKNbWZN2+edE5brVbD09PzjtaTiIioPkwe1L6+voiPj8fBgwfxwgsvYPz48Th58qQ0X6FQGNULIWpMq656TW31t3qfWbNmQavVSo+0tLTbXSUiIqIGY/KgtrS0RKdOndC3b1/MmzcPPXr0wCeffAKNRgMANfZ6s7Ozpb1sjUaDsrIy5Obm3rQmKyurxnJzcnJuegMRlUoljUavehARETU2kwd1dUII6HQ6eHt7Q6PRYOfOndK8srIy7Nu3D8HBwQCAPn36wMLCwqgmIyMDCQkJUk1QUBC0Wi0OHz4s1Rw6dAharVaqISIikiuTjvp+8803MWzYMHh6eqKgoAAbN27E3r17ER0dDYVCgYiICERFRcHHxwc+Pj6IioqCjY0NwsLCAABqtRoTJ07Eq6++CicnJzg6OmLmzJkICAiQRoH7+flh6NChmDRpElasWAEAmDx5MkJDQznim4iIZM+kQZ2VlYXw8HBkZGRArVaje/fuiI6OxqBBgwAAr732GkpKSvDiiy8iNzcXgYGB2LFjB+zs7KT3WLRoEZRKJUaPHo2SkhIMGDAAa9asgbm5uVSzfv16TJ8+XRodPnLkSCxdurRxV5aIiKgeTBrUq1atuul8hUKByMhIREZG3rDGysoKS5YswZIlS25Y4+joiHXr1tW3TSIiIpOR3TlqIiIi+geDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyZjS1A20RKmpqbh8+XK9X+/s7AwvL68G7IiIiOSKQd3IUlNT0cXPDyXFxfV+D2sbG5xKSmJYExG1AAzqRnb58mWUFBdj7Osfws2rY51fn5X6N9Z/8H+4fPkyg5qIqAVgUJuIm1dHtPXpZuo2iIhI5jiYjIiISMYY1ERERDLGoCYiIpIxBjUREZGMMaiJiIhkjEFNREQkYwxqIiIiGWNQExERyRiDmoiISMYY1ERERDLGoCYiIpIxBjUREZGMmTSo582bh3vuuQd2dnZwdXXFY489huTkZKMaIQQiIyPh4eEBa2trhISEIDEx0ahGp9Nh2rRpcHZ2hq2tLUaOHIn09HSjmtzcXISHh0OtVkOtViM8PBx5eXl3exWJiIjuiEmDet++fZg6dSoOHjyInTt3oqKiAoMHD0ZRUZFUs2DBAixcuBBLly5FbGwsNBoNBg0ahIKCAqkmIiICmzdvxsaNG7F//34UFhYiNDQUer1eqgkLC0N8fDyio6MRHR2N+Ph4hIeHN+r6EhER1ZVJb3MZHR1t9Hz16tVwdXVFXFwcHnzwQQghsHjxYsyePRujRo0CAKxduxZubm7YsGEDpkyZAq1Wi1WrVuGbb77BwIEDAQDr1q2Dp6cndu3ahSFDhiApKQnR0dE4ePAgAgMDAQArV65EUFAQkpOT4evr27grTkREdJtkdY5aq9UCABwdHQEAKSkpyMzMxODBg6UalUqF/v3748CBAwCAuLg4lJeXG9V4eHjA399fqomJiYFarZZCGgD69esHtVot1VSn0+mQn59v9CAiImpssglqIQReeeUV3H///fD39wcAZGZmAgDc3NyMat3c3KR5mZmZsLS0hIODw01rXF1dayzT1dVVqqlu3rx50vlstVoNT0/PO1tBIiKiepBNUL/00ks4fvw4vv322xrzFAqF0XMhRI1p1VWvqa3+Zu8za9YsaLVa6ZGWlnY7q0FERNSgZBHU06ZNw9atW7Fnzx60bdtWmq7RaACgxl5vdna2tJet0WhQVlaG3Nzcm9ZkZWXVWG5OTk6NvfUqKpUK9vb2Rg8iIqLGZtKgFkLgpZdewqZNm7B79254e3sbzff29oZGo8HOnTulaWVlZdi3bx+Cg4MBAH369IGFhYVRTUZGBhISEqSaoKAgaLVaHD58WKo5dOgQtFqtVENERCRHJh31PXXqVGzYsAE///wz7OzspD1ntVoNa2trKBQKREREICoqCj4+PvDx8UFUVBRsbGwQFhYm1U6cOBGvvvoqnJyc4OjoiJkzZyIgIEAaBe7n54ehQ4di0qRJWLFiBQBg8uTJCA0N5YhvIiKSNZMG9fLlywEAISEhRtNXr16NCRMmAABee+01lJSU4MUXX0Rubi4CAwOxY8cO2NnZSfWLFi2CUqnE6NGjUVJSggEDBmDNmjUwNzeXatavX4/p06dLo8NHjhyJpUuX3t0VJCIiukMmDWohxC1rFAoFIiMjERkZecMaKysrLFmyBEuWLLlhjaOjI9atW1efNomIqAUTQiBDW4r03BKkZCvRquewRl2+SYOaiIhIzorLKrAnOQdnswuvTTGDtXfvRu1BFqO+iYiI5Ca3qAzrD6XibHYhzBSAj2sr9HCoQN7+DY3aB/eoiYiIqinUVWBz/EUUl+nhaGuJIV3d4GpvhfQzV1Gek9KovTCoiYiIrlNhMODn+IsoKK1Aa2sLPNG7DWwsTReXPPRNRER0ncMpV3G5sAzWFuZ4rJdpQxpgUBMREUmy80tx5ELllS4f7uIKtbWFiTtiUBMREQGo/BrWrlPZEKJy4Fgn11ambgkAg5qIiAgAcDqrEDkFOliamyHE18XU7UgY1ERE1OLpDQIx564AAPq0czD5eenrMaiJiKjFO3kpH9qSclhbmKOnZ2tTt2OEQU1ERC2awSAQe+EqAOBeb0dYKuUVjfLqhoiIqJGdzSlEQWkFrC3M4e9hb+p2amBQExFRiyWEwNHUyq9jBbRVQ2kuv1iUX0dERESN5JK2FFn5OpibKdCjrdrU7dSKQU1ERC3WsbQ8AICfxk5WI72vx6AmIqIWqbisAn/nVN6+snvb1qZt5iYY1ERE1CIlZRTAIAA3exVc7FSmbueGGNRERNTiCAGcuKgFAPi3kee56SoMaiIianFydApoS8phaW6Gzq52pm7nphjURETU4qQWVcZfZ7dWsrvASXXy7o6IiKihmVvgYnFl/HXRyO8CJ9UxqImIqEWx7tgXFUIBOyslPFpbmbqdW2JQExFRi2LbNQQA0NnNDgqFwrTN3AYGNRERtRhFZQbYdLwHAODrJu9BZFUY1ERE1GIcvFgKhdIS9hYGOLeyNHU7t4VBTURELcafqSUAAE8bQ5M47A0wqImIqIXIzi9FQnYZAMDT1mDibm4fg5qIiFqEbcczYBBAafpJ2Mrz/hu1YlATEVGL8POxSwCAopP7TNxJ3TCoiYio2Uu9UoxjaXkwUwDFyftN3U6dMKiJiKjZi07MAAD4u1rCUKw1cTd1w6AmIqJmLzohEwAQ2Eb+VyKrjkFNRETNWlZ+KY6m5gFgUBMREcnOjpNZAIDeXq3haG1u4m7qjkFNRETN2m/XDnsP9deYuJP6YVATEVGzlVdchphzVwAAQ7oxqImIiGRlV1I29AaBLho7tHOyNXU79cKgJiKiZiu6iR/2BhjURETUTBXpKvDHmRwADGoiIiLZ2Zucg7IKA9o72TSZe0/XhkFNRETNUnRi5WHvIf6aJnNLy9owqImIqNnRVeix51Q2gKY72rsKg5qIiJqdA2evoFBXATd7FXq2bW3qdu4Ig5qIiJqdqtHeQ7ppYGbWdA97AwxqIiJqZir0BuxMqrxs6NAmftgbAJSmboCImja9QeCPMzn48/RlHEy+ArdxH+KPLCU6mF9Be2dbaOyb3k0QqGmLPZ+Lq0VlaG1jgXu9HU3dzh1jUBNRve08mYUPfzuF01mF0jSrNn7I0QE5KVdxKOUq2jnaILiTE1ztGNjUOH67Ntp7oJ8blOZN/8Bx018DImp0peV6/N8PxzDp6yM4nVUIeyslnrnXCzMCWyP7p/fQy7ECPq6tYKYALlwtxsbYNBxNzYUQwtStUzNnMIh/rkbWDA57AyYO6j/++AOPPPIIPDw8oFAosGXLFqP5QghERkbCw8MD1tbWCAkJQWJiolGNTqfDtGnT4OzsDFtbW4wcORLp6elGNbm5uQgPD4darYZarUZ4eDjy8vLu8toRNU9XCnV48vMD+CEuHWYK4N/9O+LP1x/GvFEB6N/OGiVnD6FDKwOGB7jj2aD26OTSCkIAf565jN8Ss6A3MKzp7jl+UYvM/FLYWJrjfh9nU7fTIEwa1EVFRejRoweWLl1a6/wFCxZg4cKFWLp0KWJjY6HRaDBo0CAUFBRINREREdi8eTM2btyI/fv3o7CwEKGhodDr9VJNWFgY4uPjER0djejoaMTHxyM8PPyurx9Rc3OlUIewlYeQcDEfTraWWDcxEG8M6wK1tUWt9WprCwwP0CCkswvMFEByVgF+S8yEgWFNd0nVYe+HurjCyqLp3Xu6NiY9Rz1s2DAMGzas1nlCCCxevBizZ8/GqFGjAABr166Fm5sbNmzYgClTpkCr1WLVqlX45ptvMHDgQADAunXr4OnpiV27dmHIkCFISkpCdHQ0Dh48iMDAQADAypUrERQUhOTkZPj6+jbOyhI1cYW6CoxbdRjJWQVwtVNh4+R+6ODS6pavUygU6OHZGnbWSvxyPANnsgthbpaFwV3dmvTVokh+hGh+h70BGZ+jTklJQWZmJgYPHixNU6lU6N+/Pw4cOAAAiIuLQ3l5uVGNh4cH/P39pZqYmBio1WoppAGgX79+UKvVUk1tdDod8vPzjR5ELZXBIPDyd/FIysiHcysVvr3NkL5eB+dWGBHgDoUCOJVZgCMXcu9St9RSnckuRMrlIliamyHE18XU7TQY2QZ1ZmblX0Vubm5G093c3KR5mZmZsLS0hIODw01rXF1da7y/q6urVFObefPmSee01Wo1PD0972h9iJqyxbtOY+fJLFgqzfDFs33QsY4hXaWDSyv071z5C/TA31eQcrmoIdukFu7XE5W/0+/3cYadVe2nY5oi2QZ1leqHxoQQtzxcVr2mtvpbvc+sWbOg1WqlR1paWh07J2oeDpy9jCV7zgIA5j0egN5eDrd4xc31aNsaAW3UAIAdJzNRqKu44x6JAODXhAwATfuWlrWRbVBrNJUbuvpeb3Z2trSXrdFoUFZWhtzc3JvWZGVl1Xj/nJycGnvr11OpVLC3tzd6ELU0uUVlePn7eAgBPHOvJ57o07ZB3rd/Zxe42KlQWm7AjsRMfm2L7tjfOYU4lVkApZkCg7ve+Hd7UyTboPb29oZGo8HOnTulaWVlZdi3bx+Cg4MBAH369IGFhYVRTUZGBhISEqSaoKAgaLVaHD58WKo5dOgQtFqtVENEtfvPzwnIytehg4st3grt2mDva26mwLBuGijNFEjLLUF8Wl6DvTe1TL+eqNybDu7kjNY2libupmGZdNR3YWEhzp49Kz1PSUlBfHw8HB0d4eXlhYiICERFRcHHxwc+Pj6IioqCjY0NwsLCAABqtRoTJ07Eq6++CicnJzg6OmLmzJkICAiQRoH7+flh6NChmDRpElasWAEAmDx5MkJDQznim+gmdiRm4pfjGTA3U+CTp3vBxrJhf1042FriAR9n7EnOwYG/r9R5cBrR9X65dn56REDzOuwNmDiojxw5goceekh6/sorrwAAxo8fjzVr1uC1115DSUkJXnzxReTm5iIwMBA7duyAnZ2d9JpFixZBqVRi9OjRKCkpwYABA7BmzRqYm//z/bn169dj+vTp0ujwkSNH3vC720QE5JeW462fEwAAkx/sgIC26ruynIA2apzOKsTFvBLsPpWNvrZ3ZTHUzKVcLkJSRj7MzRQY1JVB3aBCQkJuem5KoVAgMjISkZGRN6yxsrLCkiVLsGTJkhvWODo6Yt26dXfSKlGL8mF0MrLydfB2tsWMAT53bTkKhQID/Fyx/lAqUq8Ww00h27NxJGPbqw57d3SCo23zOuwNyPgcNRGZRsJFLdYfugAAeP9x/7t+dScHG0vc277yDkcJeeZQWKju6vKo+aka7T08wN3EndwdDGoikhgMAm//nACDAB7p4YHgjo1zreTeXq1hb6VEiV4B+35PNcoyqXlIvVKMhIuVh72b22jvKgxqIpJsib+Io6l5sLU0x+zhfo22XKW5GR7wqbwQivreUcgq5Her6fZsv7Y33a+DI5xaNc+jMQxqIgJQeevKj35LBgBMfbgTNOrGvX90RxdbuKgMUCgtsfZYwa1fQIR/zk8318PeAIOaiK5Ze+A8LmlL4a62wnP3eTf68hUKBXo46CEMehy8WIoDZy83eg/UtKRdLcbxdC3MFMCQZnQTjuoY1ESE3KIyLL12mdBXB/ua7PaAakuBgv9tBwC889+TqNAbTNIHNQ0/x18EAPTr4ATnZnrYG2BQExGAz/acRUFpBbpo7PB4rzYm7UW7fz1aWSqQnFWAH+LSTdoLyZcQApv+VxnUpv7M3m0MaqIWLu1qMb6Oqfw61qzhfjA3M+09og2lhXiqa+VFjRbuPI0i3rSDanHiohbncoqgUpo1u5twVMegJmrhPtqRjDK9Afd3csaDPo3zdaxbGdrRBl6ONsgp0GHln+dM3Q7J0KajlXvTg7tpmtUtLWvDoCZqwU6ka/Fz/CUAwBvDutzyFrKNxcJcgdeGVl6L/4s/ziE7v9TEHZGclOsN+O+xys/tqGZ+2BtgUBO1WEIIRG1PAlB5js+/zd25nnd9jQhwR0/P1igu02PRrtOmbodkZP+Zy7hSVAYnW0vcL5OjQHcTg5qohdp7Ogcx567A0twMrwzqbOp2alAoFPjPiMqLrnwXm4bTWfxuNVWqGkT2SA8PWJg3/xhr/msoM3P/vAr3fy3BH1lK7ErKwsmMfA6WoUanNwh88OspAMD44HbwdLQxcUe169veEUO6ucEggPnX+qWWraC0HDsSK29pOap38z/sDZj47lktUZq2Apau3sjRATmX8pF4KR8KAO2dbdHLs7Vsf2FS87LpaDpOZRbA3kqJqQ91MnU7N/X60C74PSkbu09l48DZywju1PwPddKN/ZqQCV2FAR1cbBEgs9M1dwv3qBvZG/c7IOv7t3GPUwX6tHOAm70KApX3U930v4vY8r+LuFKoM3Wb1IyVluvx8Y7Kc74vPdwJrW3kfVvADi6tMDbQCwDw/vYkGAw3vjUuNX9brh32HtWrjWwGP95tDOpG5t3aAqUpR+FlW/l1mDH3eCG8Xzt0b6OGmQK4cLUY3x5OQ+z5q/yFRHfFV3+lIDO/FG1aW+PZoPambue2TB/gAzuVEomX8vHzsYumbodMJPVKMQ78fQUA8GjPlnHYG2BQy4KjrSUe6uKK8H7t0N7JBnohcODvK9gSfxElZXpTt0fNyNWiMizf8zcAYOaQzia7VGhdObVS4d8hHQEAH/12GqXl/P+iJdoYmwoAeMDHuUWdJmRQy0hrG0uM7OGBgX6usDBXIC23BN/GpuIyD4VTA1my+wwKdBXo6m6PR3s0rT2Sifd7w11thYt5JVhz4Lyp26FGVq434PsjlZeUDbvXy8TdNC4GtcwoFAp081BjdF9PqK0tUFBagR+OpCM9t9jUrVETd+FKEdYdrLxU6JvD/WBm4kuF1pWVhTlmDq68CMpnu8/ialGZiTuixrTrZBYuF+rg3EqFgV3dTN1Oo2JQy5RzKxXG3OMJD7UVyvQGbPnfJaRcLjJ1W9SELYhORrle4MHOLk32IhGP92qDru72KNBV4NPfz5i6HWpE6w9VHvYe3bdti/ju9PVa1to2MVYW5ni8Vxt0dLGFXgj8cjwDmSVNay+I5OFwylX8ciIDZgpg1rAupm6n3szMFHhzeOVFUNYdvIDz/OO1RTiTVYD9Zy/DTAE808IOewMMatlTmpthmL+7FNYxOUpYte9l6raoCTEYBN7dlggAGHOvF/zc7U3c0Z2538cZ/Tu7oMIgsOA3XgSlJagakzDQz61FDSKrwqBuAszNFFJYG6CAy6j/ID6TA8zo9vx4NB0JF/Nhp1LK8lKh9TFreBeYKYDtJzIRd+Gqqduhu0hbXC7dKetf93mbuBvTYFA3EVVh7W5tgJmFCh/8lYv/peaaui2SuUJdBT78LRlA5XeRnVupTNxRw+iiscdTfTwBAO//kgQheM2B5mpjbCpKyvXoorFDvw6Opm7HJBjUTYi5mQL9nCtQcu4IdHqB59bE4u+cQlO3RTK2bM9Z5BTo0N7JBuOD25u6nQb1yuDOsLYwx9HUPEQnZJq6HboLdBV6fPVXCgDgufu9W8yVyKpjUDcxZgogZ8t8dHK0QG5xOZ5ddRhZvFcv1SL1SjG+3F/5S272iK6wVDav/93d7K0w6YHKQ6EfRJ+CroIXQWluNh29iKx8HdzVVnisBV2JrLrm9X9uCyHKSzH7fgd4O9viYl4Jxn91GNqSclO3RTIihMB/fk5AWYUB93VywkA/V1O3dFdM7t8Rzq1UOH+lGMv3/m3qdqgBVegN+Hxf5c900gMdmt0fmnXRcte8iVNbmePr5+6Fi50KpzILMOnrI7ysIkm2HruEP07nwFJphvce9W+2hwxbqZSY80hXAMCyPX/jbDbvWd1c/HIiAxeuFMPBxgJj7vU0dTsmxaBuwjwdbbD2X/fCTqXE4ZSriNgYDz1v5NHi5RaV4d3/ngQATH+4Ezq4tDJxR3dXaHd3POTrgjK9AW9uSuDNbJqBcr0Bi3dVXtBm4v3esLFs2XdkZlA3cV097PHFs31haW6G6MRMvPVzAkfAtnDvb0/ClaIy+LrZYfKDHU3dzl2nUCjw3mP+sLE0x+HzV/HdkTRTt0R36Ke4dKRcLoKTrSUmtNCvZF2PQd0MBHV0wuIxPaFQABsOpWLhztOmbolM5K+zl/FjXDoUCmDeEwEt5rxeWwcbvHrtOuBR25OQzQGWTVZpuR6fXLs87IsPdUIrVcvemwYY1M3G8AB3zH3MHwCwZPdZfHVttC+1HMVlFXhz8wkAwLP92qG3l4OJO2pcE4Lbo3tbNQpKK/D2z4k8stRErf7rPDK0pXBXW2FsYMu7XGhtGNTNyNjAdpg5uPLKU+9uO4nN/0s3cUfUmN7bdhIXrhTDXW2FmUN8Td1OozM3U2D+qO5QmikQnZiJH+P4+W9qsvJLsWR35d70zMG+TeZ+6Xcbg7qZmfpQJ/zrvvYAgJk/HMfuU1mmbYgaxW+Jmfj2cBoUCuDj0T1gZ2Vh6pZMoquHPV659sdq5NZEXLjCm3Y0JfN/PYXiMj16ebXG471a7vemq2NQNzMKhQJvjeiKx3u1gd4g8MK6o4g9z2shN2fpucV4/afjAIDJD3RAcMemeQvLhjLlwY6419sRRWV6TPv2f7wQShMR8/cVbP7fRSgUQOQj3Zrc/dLvJgZ1M2RmpsCCJ7vj4S6u0FUY8NzqWBzldcGbJV2FHlPXH0VecTm6t1VLe5MtmbmZAoue7onWNhY4nq7Fe9tOmroluoXisgrpj81n7vVCD8/Wpm1IZhjUzZSFuRk+C+uNe70dUaCrwLOrDnPPupkRQuCd/57EsXQt1NYW+CysN1RKntMDgDatrbHo6cpvQqw7mIqfeL5a1j78LRmpV4vhobZq0vdLv1sY1M2YtaU51vzrHgR1cEKhrgLjvzqMg+eumLotaiBrDpzHhkOpUCiAxU/3bJH36b2Zh3xdMe1hHwDArE0n+IeqTO1Nzsbqv84DAOY90b3Fjq+4GQZ1M2djqcRXE+7BAz7OKC7TY8Lqw/jjdI6p26I79HtSlnRId9awLnioS/O8lvedihjgg6HdNCjTGzD56yNIuczBZXKSoS3By9/FAwDC+7VD/84upm1IphjULYC1pTlWPtsXIb4uKC034Lk1sdh4ONXUbVE9HTx3BS+uPwqDAJ7u64lJD3QwdUuyZXbtfHVAGzVyi8sx7stDuJRXYuq2CJUXNpm6/ihyi8vRzcMes0f4mbol2WJQtxBWFuZYEd4Hj/b0QIVB4I1NJzDv1yReF7mJibuQi4lrYqGrMGCgnyvmPt58b7jRUKwtzfHVhHuku82NW3WIVy4zMYNBYOYPx3A0NQ92Vkp8Ftab35m+CQZ1C6JSmmPx0z0xY0DlebsV+87hxfVHUaSrMHFndDsOnL2M8FWHUFSmR1AHJywN6w0Lc/4vfDtc7FRY93wgPNRWOJdThKdWxCDtarGp22qRhBCYH30K245nQGmmwOfj+qC9s62p25I1/l/eyEZ9nwGv1/6Ln0x05FmhUODlQZ2x+Ome0o08Qpfsx/H0PNM0RLdl67FLmLAmFsVletzfyRmrJvSV5R6IqT/fN9OmtTU2Tg6Cp6M1LlwpxpOfH0DCRa2p22pRhBD4IDoZX/xxDgAwb1QA7uvUtL73/1Mq4PXafzHq+4xGWyaD2gQqD1Wa9nDlY73aYMOkQLirrZByuQijlh3Asr1neZtMmTEYBBbuPI3p3/4PZRUGDO7qhi/H95X1bf/k8Pm+ES8nG/wwJRg+rq2Qla/DU5/HYPuJxvuF25LpDQKRWxPx+b6/AQDvjOyGp/o2xftMKxr9dBODugXr294R0TMexIgAd1QYBBZEJ+OZLw4iKSPf1K0RgOz8UoR/dQifXruT0OQHO2D5uD6y3JNuSjRqK/z4QjAe8HFGSbkeL64/ird/TkBpOa9gdrfkl5Zj0tdHsDbmAgDg3Ue7YXxwe9M21YQwqFs4tY0Flob1wodPdpfu5zvi0z8xa9MJXC7Umbq9FkkIgR/j0jF48R/46+wVWFuY46OneuDN4X4w52UVG4Ta2gKrJ9yDKQ9Wjpj/OuYCQpfs53et74KjqbkY8emf2H0qGyqlGZaP7Y1ng9qbuq0mRb7Hz6jRKBQKPNXXE/06OGF+9Cn8cjwD3x5OxbZjl/D8Ax0wrp8XnFqpTN1mixCfloeo7Uk4nFIZGF3d7fHpM73QybWViTtrfpTmZpg13A9BHZ0w84fjOJtdiKc+j8Go3m3w6mBftGltbeoWm7SC0nIs3nUGaw6ch94g0NbBGkvDeqMnLw9aZwxqkng62uCzsN4YH3QV725LRMLFfCzadRrL9p7F473a4Ln7vdHZzc7UbTY7QgjEXcjF5/v+xq6kbACASmmGiIGd8fwD3hzZfZeF+Lri91f6Y96vSdgYm4ZNRy9i2/EMPNWnLSY90IEjkuuotFyPDYdSsWzv39JRuZE9PDD3cX/Y86pj9cKgphru9XbE1qn347/HL+HLP1Nw4qIWG2PTsDE2Dd3bqjHM3x3DAzRo58RfYHciU1uK3xIz8V1sGk5eGxegUABP9G6LVwZ1hgf36BqN2sYC85/ojmfu9cK8X5Nw8NxVrD+UivWHUhHo7YjHerXBcH93qG0YNDeSeqUY3x1JxcbDabhSVAYAaOdkg3dGdkOIL6+cdydaVFAvW7YMH374ITIyMtCtWzcsXrwYDzzwgKnbkiUzMwUe7dkGI3t4IPZ8Lr7an4IdJzNxPF2L4+lafBB9Cl00dgj0dkTf9o64p70jNGorU7cta8VlFUi8lI8/T+fg91PZSLz0z6A9S6UZRvVqg0kPdkBHFx7mNpUenq3x7aR+OJxyFZ/v+xt7knNwKOUqDqVcxZyfE3G/jzP6dXDEvd5O8Pewh7IFH+0o1xtw8lI+/jidg11JWTiW/s9X3dq0tsbUhzrhyT5tYalsuduoobSYoP7uu+8QERGBZcuW4b777sOKFSswbNgwnDx5El5eXqZuT7YUCgXu9XbEvd6OyCnQYcfJTGw/kYGD567iVGYBTmUWSCM5Xe1U8HFrBR9XO3R0bYW2DtZwV1vB3d4a9tbKFnEFLYNBQFtSjvTcEqReLUZabjHOZBUi4aIWZ7ILcP233xQKoKdnazzawwOP9WqD1jaWpmucJAqFAoEdnBDYwQkX80qwNf4StvzvIpKzCrD7VDZ2n6o8PWFraQ4/d3v4uLVCJ1c7dHSxhUdra7jZWTWrz3tpuR6X8kqQnluCtNxinLyUj4SLWiRlFqCswiDVmSmA4I7OGBvohUFd3Vr0HzENrcUE9cKFCzFx4kQ8//zzAIDFixfjt99+w/LlyzFv3jwTd9c0uNipMDawHcYGtsPVojLE/H0FseevIvb8VSRl5CO7QIfsAh3+OlvzDl0qpRnU1hawt7aAvZVS+re1hTkslWawNDeDysIMlubXnivNYGmuABQKmCkAM4UCClT+F9eem1XOrpx3bb5CAQgBCFSe+63897X/Xj8dAK6fB8Ag/vk3rtUIAZRVGKCr0ENXYah8lOtRpjdAV25AfmkF8orLkFtchrzicuSVlN/0u+iudir0be+Ah7u44SFfFw7Sk7k2ra3xQkhHvBDSEacy87H/zGUcPHcVh1OuIL+0Akcu5OLIhZr3ereyMINzKxXsrCxgp1LCzqrqYQGV0gwWSjNYmFd+xi3MK/9toTSDuUKBax/xa/+99vy6z/f104F/5glU/qFoEAL6a/81iMrvLwtpGq5NF9AbKj/bJeV6lJbrUVKmR0m5HkW6CunznFtchtzi8htuHzsrJYI6OKG/rwsGd9XAxY6f57uhRQR1WVkZ4uLi8MYbbxhNHzx4MA4cOFDra3Q6HXS6f76epNVWHtbJz7+z7xgbdFWXLSzH38dj6/z6nPQUAEBcXBwKCwvr/HozMzMYDIZbF97Ga+0APNwaeLgnUOpvi/R8PS4WVOBSQQUuFVbgarEeV0sFCnQGlOiAkiIgs15LbnrUVmZwtTGDq60Sbq3M0b61BbxbK+FgZQ6gCCg6h8Sj5276Hnfys7rT19f3tQadFoAFmsPnuzadAXT2Bsa1t8LFfD3SCyqQnl+BS/kVyCiqQG6pAUVlAsU6ILUe/cuVSqmAs7UZnG3N0dZOCe9rn2c3OwtAFAO6C0j63wUk1fF9TfEZTU5OBgCkn0mErqTul5E16BSo/IzfeR4AgJ2d3a2PvogW4OLFiwKA+Ouvv4ymv//++6Jz5861vmbOnDkC13bA+OCDDz744ONuPLRa7S0zrEXsUVep/leLEOKGf8nMmjULr7zyivTcYDDg6tWrcHJyuqNzT/n5+fD09ERaWhrs7e3r/T7NHbfT7eF2ujVuo9vD7XR7Gno72dnd+iuvLSKonZ2dYW5ujsxM4wOv2dnZcHNzq/U1KpUKKpXx+ZbWrVs3WE/29vb8n+E2cDvdHm6nW+M2uj3cTrenMbdTixiWZ2lpiT59+mDnzp1G03fu3Ing4GATdUVERHRrLWKPGgBeeeUVhIeHo2/fvggKCsIXX3yB1NRU/Pvf/zZ1a0RERDfUYoL66aefxpUrV/Duu+8iIyMD/v7+2L59O9q1a9eofahUKsyZM6fGYXUyxu10e7idbo3b6PZwO90eU2wnhRBCNNrSiIiIqE5axDlqIiKipopBTUREJGMMaiIiIhljUBMREckYg/ouWL58Obp37y59IT4oKAi//vqrNF8IgcjISHh4eMDa2hohISFITEw0YcfyMG/ePCgUCkREREjTuK2AyMjIyhsvXPfQaDTSfG6jShcvXsS4cePg5OQEGxsb9OzZE3FxcdJ8biegffv2NT5LCoUCU6dOBcBtVKWiogL/+c9/4O3tDWtra3To0AHvvvuu0bXFG3Vb3ck1tKl2W7duFb/88otITk4WycnJ4s033xQWFhYiISFBCCHE/PnzhZ2dnfjpp5/EiRMnxNNPPy3c3d1Ffn6+iTs3ncOHD4v27duL7t27ixkzZkjTua0qrzvfrVs3kZGRIT2ys7Ol+dxGQly9elW0a9dOTJgwQRw6dEikpKSIXbt2ibNnz0o13E5CZGdnG32Odu7cKQCIPXv2CCG4jarMnTtXODk5iW3btomUlBTxww8/iFatWonFixdLNY25rRjUjcTBwUF8+eWXwmAwCI1GI+bPny/NKy0tFWq1Wnz++ecm7NB0CgoKhI+Pj9i5c6fo37+/FNTcVpXmzJkjevToUes8bqNKr7/+urj//vtvOJ/bqXYzZswQHTt2FAaDgdvoOiNGjBDPPfec0bRRo0aJcePGCSEa//PEQ993mV6vx8aNG1FUVISgoCCkpKQgMzMTgwcPlmpUKhX69+9/w1tuNndTp07FiBEjMHDgQKPp3Fb/OHPmDDw8PODt7Y0xY8bg3LnKW2RyG1XaunUr+vbti6eeegqurq7o1asXVq5cKc3ndqqprKwM69atw3PPPQeFQsFtdJ37778fv//+O06fPg0AOHbsGPbv34/hw4cDaPzPU4u5MlljO3HiBIKCglBaWopWrVph8+bN6Nq1q/RDrH4zEDc3N1y4cMEUrZrUxo0bERcXhyNHjtSYV3UTlZa+rQIDA/H111+jc+fOyMrKwty5cxEcHIzExERuo2vOnTuH5cuX45VXXsGbb76Jw4cPY/r06VCpVHj22We5nWqxZcsW5OXlYcKECQD4/9v1Xn/9dWi1WnTp0gXm5ubQ6/V4//338cwzzwBo/G3FoL5LfH19ER8fj7y8PPz0008YP3489u3bJ82vyy03m6u0tDTMmDEDO3bsgJWV1Q3rWvq2GjZsmPTvgIAABAUFoWPHjli7di369esHgNvIYDCgb9++iIqKAgD06tULiYmJWL58OZ599lmprqVvp+utWrUKw4YNg4eHh9F0biPgu+++w7p167BhwwZ069YN8fHxiIiIgIeHB8aPHy/VNda24qHvu8TS0hKdOnVC3759MW/ePPTo0QOffPKJNFq3LrfcbK7i4uKQnZ2NPn36QKlUQqlUYt++ffj000+hVCql7cFtZczW1hYBAQE4c+YMP0/XuLu7o2vXrkbT/Pz8kJqaCgDcTtVcuHABu3btwvPPPy9N4zb6x//93//hjTfewJgxYxAQEIDw8HC8/PLLmDdvHoDG31YM6kYihIBOp4O3tzc0Go3RLTfLysqwb9++FnfLzQEDBuDEiROIj4+XHn379sXYsWMRHx+PDh06cFvVQqfTISkpCe7u7vw8XXPfffchOTnZaNrp06elm+5wOxlbvXo1XF1dMWLECGkat9E/iouLYWZmHI/m5ubS17MafVs1+PA0ErNmzRJ//PGHSElJEcePHxdvvvmmMDMzEzt27BBCVA7rV6vVYtOmTeLEiRPimWeeaZFfgajN9aO+heC2EkKIV199Vezdu1ecO3dOHDx4UISGhgo7Oztx/vx5IQS3kRCVX+9TKpXi/fffF2fOnBHr168XNjY2Yt26dVINt1MlvV4vvLy8xOuvv15jHrdRpfHjx4s2bdpIX8/atGmTcHZ2Fq+99ppU05jbikF9Fzz33HOiXbt2wtLSUri4uIgBAwZIIS1E5dD+OXPmCI1GI1QqlXjwwQfFiRMnTNixfFQPam4rIX0/08LCQnh4eIhRo0aJxMREaT63UaX//ve/wt/fX6hUKtGlSxfxxRdfGM3ndqr022+/CQAiOTm5xjxuo0r5+flixowZwsvLS1hZWYkOHTqI2bNnC51OJ9U05rbibS6JiIhkjOeoiYiIZIxBTUREJGMMaiIiIhljUBMREckYg5qIiEjGGNREREQyxqAmIiKSMQY1ERGRjDGoiWROoVDc9FF1m8LmJCQkBBEREaZug0gWeJtLIpnLyMiQ/v3dd9/h7bffNroBhbW1tSnaqpfy8nJYWFg02+UR3Q3coyaSOY1GIz3UajUUCoXRtD/++AN9+vSBlZUVOnTogHfeeQcVFRXS6xUKBVasWIHQ0FDY2NjAz88PMTExOHv2LEJCQmBra4ugoCD8/fff0msiIyPRs2dPrFixAp6enrCxscFTTz2FvLw8o95Wr14NPz8/WFlZoUuXLli2bJk07/z581AoFPj+++8REhICKysrrFu3DleuXMEzzzyDtm3bwsbGBgEBAfj222+l102YMAH79u3DJ598Ih01OH/+PNasWYPWrVsbLX/Lli1G9/+t6vurr75Chw4doFKpIISAVqvF5MmT4erqCnt7ezz88MM4duxYA/2EiO4uBjVRE/bbb79h3LhxmD59Ok6ePIkVK1ZgzZo1eP/9943q3nvvPTz77LOIj49Hly5dEBYWhilTpmDWrFk4cuQIAOCll14yes3Zs2fx/fff47///S+io6MRHx+PqVOnSvNXrlyJ2bNn4/3330dSUhKioqLw1ltvYe3atUbv8/rrr2P69OlISkrCkCFDUFpaij59+mDbtm1ISEjA5MmTER4ejkOHDgEAPvnkEwQFBWHSpEnIyMhARkYGPD09b3ubVPX9008/IT4+HgAwYsQIZGZmYvv27YiLi0Pv3r0xYMAAXL169bbfl8hk7sqtPojorli9erVQq9XS8wceeEBERUUZ1XzzzTfC3d1deg5A/Oc//5Gex8TECABi1apV0rRvv/1WWFlZSc/nzJkjzM3NRVpamjTt119/FWZmZiIjI0MIIYSnp6fYsGGD0bLfe+89ERQUJIQQIiUlRQAQixcvvuV6DR8+XLz66qvS8+p3Uatt3YUQYvPmzeL6X2Nz5swRFhYWIjs7W5r2+++/C3t7e1FaWmr02o4dO4oVK1bcsjciU+M5aqImLC4uDrGxsUZ70Hq9HqWlpSguLoaNjQ0AoHv37tJ8Nzc3AEBAQIDRtNLSUuTn58Pe3h4A4OXlhbZt20o1QUFBMBgMSE5Ohrm5OdLS0jBx4kRMmjRJqqmoqIBarTbqsW/fvkbP9Xo95s+fj++++w4XL16ETqeDTqeDra3tnW4OAEC7du3g4uIiPY+Li0NhYSGcnJyM6kpKSowO9xPJFYOaqAkzGAx45513MGrUqBrzrKyspH9fP6Cq6pxubdMMBsMNl1VVo1AopLqVK1ciMDDQqM7c3NzoefUA/vjjj7Fo0SIsXrwYAQEBsLW1RUREBMrKym68ogDMzMwgqt2Vt7y8vEZd9eUZDAa4u7tj7969NWqrn/MmkiMGNVET1rt3byQnJ6NTp04N/t6pqam4dOkSPDw8AAAxMTEwMzND586d4ebmhjZt2uDcuXMYO3Zsnd73zz//xKOPPopx48YBqAzSM2fOwM/PT6qxtLSEXq83ep2LiwsKCgpQVFQkhXHVOeib6d27NzIzM6FUKtG+ffs69UokBwxqoibs7bffRmhoKDw9PfHUU0/BzMwMx48fx4kTJzB37tw7em8rKyuMHz8eH330EfLz8zF9+nSMHj0aGo0GQOUI6+nTp8Pe3h7Dhg2DTqfDkSNHkJubi1deeeWG79upUyf89NNPOHDgABwcHLBw4UJkZmYaBXX79u1x6NAhnD9/Hq1atYKjoyMCAwNhY2ODN998E9OmTcPhw4exZs2aW67HwIEDERQUhMceewwffPABfH19cenSJWzfvh2PPfZYjUPzRHLDUd9ETdiQIUOwbds27Ny5E/fccw/69euHhQsXol27dnf83p06dcKoUaMwfPhwDB48GP7+/kZfv3r++efx5ZdfYs2aNQgICED//v2xZs0aeHt73/R933rrLfTu3RtDhgxBSEgINBoNHnvsMaOamTNnwtzcHF27doWLiwtSU1Ph6OiIdevWYfv27dJXuiIjI2+5HgqFAtu3b8eDDz6I5557Dp07d8aYMWNw/vx56Xw9kZwpRPWTPkTU4kVGRmLLli23dWiZiO4u7lETERHJGIOaiIhIxnjom4iISMa4R01ERCRjDGoiIiIZY1ATERHJGIOaiIhIxhjUREREMsagJiIikjEGNRERkYwxqImIiGSMQU1ERCRj/w9HUxs+OVdligAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Creating a histogram to examine the distribution oftemperatures.\n",
    "\n",
    "sns.displot(data['temperature'], kde=True, rug=True)\n",
    "\n",
    "# Add title and labels\n",
    "plt.title('Temperature Distribution Plot')\n",
    "plt.xlabel('Temperature')\n",
    "plt.ylabel('Counts')\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Investigating the Bar Coupons**\n",
    "\n",
    "Now, we will lead you through an exploration of just the bar related coupons.  \n",
    "\n",
    "1. Create a new `DataFrame` that contains just the bar coupons.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>CoffeeHouse</th>\n",
       "      <th>CarryAway</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Kid(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Home</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>6PM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Work</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>7AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        destination passanger weather  temperature  time coupon expiration  \\\n",
       "9   No Urgent Place    Kid(s)   Sunny           80  10AM    Bar         1d   \n",
       "13             Home     Alone   Sunny           55   6PM    Bar         1d   \n",
       "17             Work     Alone   Sunny           55   7AM    Bar         1d   \n",
       "\n",
       "    gender age      maritalStatus  ...  CoffeeHouse CarryAway  \\\n",
       "9   Female  21  Unmarried partner  ...        never       1~3   \n",
       "13  Female  21  Unmarried partner  ...        never       1~3   \n",
       "17  Female  21  Unmarried partner  ...        never       1~3   \n",
       "\n",
       "   RestaurantLessThan20 Restaurant20To50 toCoupon_GEQ5min toCoupon_GEQ15min  \\\n",
       "9                   4~8              1~3                1                 1   \n",
       "13                  4~8              1~3                1                 0   \n",
       "17                  4~8              1~3                1                 1   \n",
       "\n",
       "   toCoupon_GEQ25min direction_same direction_opp  Y  \n",
       "9                  0              0             1  0  \n",
       "13                 0              1             0  1  \n",
       "17                 1              0             1  0  \n",
       "\n",
       "[3 rows x 25 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filtering and creating a new data frame for bar coupons only\n",
    "\n",
    "bar_coupons= data[data['coupon'] == 'Bar']\n",
    "bar_coupons.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. What proportion of bar coupons were accepted?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1190</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>827</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index     Y\n",
       "0      0  1190\n",
       "1      1   827"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Getting counts for 1-accpted and 0-did not accept in the Y column\n",
    "y_column=bar_coupons['Y'].value_counts().reset_index()\n",
    "y_column.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "41% of the total observations chose to accept the bar coupon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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FN3vPj4+YtCgQeLs2bMl1rlkyRLRsGFDodFoRKNGjcSqVavKnMU2a9YsMXPmTBEaGipcXV1Fy5YtxZYtW0qsc9++faJHjx7G11T79u3Fhg0bTJYp67Ow6LVd2oxoZ6IQoozxeDILhUKBKVOmGP+CJ3IUu3fvRvfu3fHLL7/cc2dha5o8eTIOHz6MY8eOWeX2vvrqK7z88svIysoqc583InOIjY1F7dq18d///rfMnd3JvLiJjYgcxty5c61yOxkZGYiKisLixYvRpEkTliMiB8SdtImIKujEiRMYPHgwXF1dS3wdEBE5Bm5iIyIiIiqGI0hERERExbAgERERERXDgkRERERUDAsSERERUTEsSERERETFsCARERERFcOCRERERFQMCxIRERFRMSxIRERERMWwIBEREREVw4JEREREVAwLEhEREVExLEhERERExbAgERERERXDgkRERERUDAsSERERUTEsSERERETFsCARERERFcOCRERERFQMCxIRERFRMSxIRERERMWwIBEREREVw4JEREREVAwLEhEREVExLEhERERExahkByAi+6Mt0CPudi6SM/OQqS1AllaHLG0B7mh1yMor/H+mVmc8v+jfnDw99EJAbxAQAtALAYMQ2BexHKFxmwEXJeCiAhRKwMXln/8r1YBbFcCzKuAR8Pe/Vf/+1/+u//99uZJvbURUOXwXISITQgikZOUh7nYu4m9rEX879+//5yI+o/C8tOx8c98oIPSAXg/oy1p3HJBSnpUpAI1PsRIVAHhVAwLqAYENgKr1AVcPM/4CRORoWJCInJROb8DVW9k4n5iFC4mZuJCYhcvJdxB/W4t8vUF2vEoQgPZ24Sn1chnLKADfMCAwsrAwBUYWnqrWBzRVrJiViGwVCxKRE0jIyP27CBWezidm4UryHTsvQpUhgNvXC0+Xtppe5F3jrtJ0178e/nKiEpEULEhEDiZTW4Bj19JxJCYNx6+nIzohCxm5BbJj2Y+s+MLT1V2m53sGAjVaAbU6ATU7AzVaFO4zRUQOiQWJyM4lZWrxZ0wajsam4c/YdFxIzIRByE7lgLJTgEtbCk8A4OoNhLcDanX+uzC15M7hRA6Er2YiO3M5+c7fZSgNR2LTcCMtV3Yk55SfBVzeXngCAFcvIKztP4UppFXh7DsiskssSEQ2Ljdfj/2Xb2FHdBJ2XUhGUmae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\n",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Data\n",
    "labels = ['Rejected', 'Accepted']\n",
    "sizes = [1190, 827]\n",
    "\n",
    "# Create the pie chart\n",
    "plt.figure(figsize=(6, 6))\n",
    "plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)\n",
    "\n",
    "# Equal aspect ratio ensures that pie is drawn as a circle\n",
    "plt.axis('equal')\n",
    "\n",
    "# Title of the pie chart\n",
    "plt.title('Proportion of Riders Accepted/Rejected the Bar Coupon')\n",
    "\n",
    "# Display the pie chart\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Compare the acceptance rate between those who went to a bar 3 or fewer times a month to those who went more.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\agnek\\AppData\\Local\\Temp\\ipykernel_6292\\1264692419.py:12: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  bar_coupons['frequency'] = bar_coupons['Bar'].map(frequency_mapping)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>CarryAway</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "      <th>frequency</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Kid(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>less3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Home</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>6PM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>less3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Work</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>7AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>less3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        destination passanger weather  temperature  time coupon expiration  \\\n",
       "9   No Urgent Place    Kid(s)   Sunny           80  10AM    Bar         1d   \n",
       "13             Home     Alone   Sunny           55   6PM    Bar         1d   \n",
       "17             Work     Alone   Sunny           55   7AM    Bar         1d   \n",
       "\n",
       "    gender age      maritalStatus  ...  CarryAway RestaurantLessThan20  \\\n",
       "9   Female  21  Unmarried partner  ...        1~3                  4~8   \n",
       "13  Female  21  Unmarried partner  ...        1~3                  4~8   \n",
       "17  Female  21  Unmarried partner  ...        1~3                  4~8   \n",
       "\n",
       "   Restaurant20To50 toCoupon_GEQ5min toCoupon_GEQ15min toCoupon_GEQ25min  \\\n",
       "9               1~3                1                 1                 0   \n",
       "13              1~3                1                 0                 0   \n",
       "17              1~3                1                 1                 1   \n",
       "\n",
       "   direction_same direction_opp  Y  frequency  \n",
       "9               0             1  0      less3  \n",
       "13              1             0  1      less3  \n",
       "17              0             1  0      less3  \n",
       "\n",
       "[3 rows x 26 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mapping values to populate a new frequency column\n",
    "\n",
    "frequency_mapping = {\n",
    "    'never': 'less3', #3 or fewer times\n",
    "    'less1': 'less3',\n",
    "    '1~3': 'less3',\n",
    "    '4~8': '3plus',  # More than 3 times\n",
    "    'gt8': '3plus'\n",
    "}\n",
    "\n",
    "# Use map function to apply the mapping and create the new column\n",
    "bar_coupons['frequency'] = bar_coupons['Bar'].map(frequency_mapping)\n",
    "\n",
    "# Display the updated DataFrame\n",
    "bar_coupons.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "frequency  Y\n",
       "3plus      0      46\n",
       "           1     153\n",
       "less3      0    1144\n",
       "           1     674\n",
       "dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculating acceptance rates for selected columns \n",
    "selected_columns = bar_coupons[['frequency', 'Y']]\n",
    "grouped = selected_columns.groupby(['frequency', 'Y']).value_counts()\n",
    "\n",
    "# Display the result\n",
    "grouped.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Interestingly, the acceptance rate for individuals who visit the bar more than three times a month is 4.4 times lower than for those who visit the bar three or fewer times a month. This discrepancy suggests that the coupon might have functioned as both an incentive and a reminder for the less frequent bar visitors. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Compare the acceptance rate between drivers who go to a bar more than once a month and are over the age of 25 to the all others.  Is there a difference?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\agnek\\AppData\\Local\\Temp\\ipykernel_6292\\577414784.py:12: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  bar_coupons['frequency2'] = bar_coupons['Bar'].map(frequency_mapping2)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "      <th>frequency</th>\n",
       "      <th>frequency2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Kid(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>less3</td>\n",
       "      <td>less1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Home</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>6PM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>less3</td>\n",
       "      <td>less1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Work</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>7AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>less3</td>\n",
       "      <td>less1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 27 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        destination passanger weather  temperature  time coupon expiration  \\\n",
       "9   No Urgent Place    Kid(s)   Sunny           80  10AM    Bar         1d   \n",
       "13             Home     Alone   Sunny           55   6PM    Bar         1d   \n",
       "17             Work     Alone   Sunny           55   7AM    Bar         1d   \n",
       "\n",
       "    gender age      maritalStatus  ...  RestaurantLessThan20 Restaurant20To50  \\\n",
       "9   Female  21  Unmarried partner  ...                   4~8              1~3   \n",
       "13  Female  21  Unmarried partner  ...                   4~8              1~3   \n",
       "17  Female  21  Unmarried partner  ...                   4~8              1~3   \n",
       "\n",
       "   toCoupon_GEQ5min toCoupon_GEQ15min toCoupon_GEQ25min direction_same  \\\n",
       "9                 1                 1                 0              0   \n",
       "13                1                 0                 0              1   \n",
       "17                1                 1                 1              0   \n",
       "\n",
       "   direction_opp  Y frequency  frequency2  \n",
       "9              1  0     less3       less1  \n",
       "13             0  1     less3       less1  \n",
       "17             1  0     less3       less1  \n",
       "\n",
       "[3 rows x 27 columns]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mapping values to populate a new frequency2 column\n",
    "\n",
    "frequency_mapping2 = {\n",
    "    'never': 'less1', #one or less\n",
    "    'less1': 'less1',\n",
    "    '1~3': '1plus',\n",
    "    '4~8': '1plus',\n",
    "    'gt8': '1plus'  # more than once\n",
    "}\n",
    "\n",
    "# Use map function to apply the mapping and create the new column\n",
    "bar_coupons['frequency2'] = bar_coupons['Bar'].map(frequency_mapping2)\n",
    "\n",
    "# Display the updated DataFrame\n",
    "bar_coupons.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21         417\n",
       "26         395\n",
       "31         339\n",
       "50plus     283\n",
       "36         209\n",
       "41         178\n",
       "46         109\n",
       "below21     87\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Reviewing age groups and their distribution\n",
    "bar_coupons['age'].value_counts()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    150\n",
       "0    103\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Setting up the filter for age under 25\n",
    "\n",
    "under_25= bar_coupons[(bar_coupons['age'] == 'below21') | (bar_coupons['age'] == '21') & (bar_coupons['frequency2'] == '1plus')]\n",
    "under_25['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    756\n",
       "1    541\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Setting up the filter for age over 25\n",
    "\n",
    "over_25= bar_coupons[(bar_coupons['age'] == '26') | \n",
    "                     (bar_coupons['age'] == '31') |\n",
    "                     (bar_coupons['age'] == '36') |\n",
    "                     (bar_coupons['age'] == '41') |\n",
    "                     (bar_coupons['age'] == '46') |\n",
    "                     (bar_coupons['age'] == '50plus') &\n",
    "                     (bar_coupons['frequency2'] == '1plus')]\n",
    "over_25['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Among respondents aged 25 or younger, 59% who reported visiting the bar more than once a month accepted the coupon. In contrast, 42% of respondents aged 26 or older with the same bar visitation frequency accepted the coupon. This indicates that both age and bar visitation frequency significantly influence bar coupon acceptance rates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5. Use the same process to compare the acceptance rate between drivers who go to bars more than once a month and had passengers that were not a kid and had occupations other than farming, fishing, or forestry. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unemployed                                   301\n",
       "Student                                      251\n",
       "Computer & Mathematical                      232\n",
       "Sales & Related                              178\n",
       "Education&Training&Library                   140\n",
       "Management                                   119\n",
       "Office & Administrative Support              105\n",
       "Arts Design Entertainment Sports & Media     100\n",
       "Business & Financial                          89\n",
       "Retired                                       75\n",
       "Food Preparation & Serving Related            48\n",
       "Community & Social Services                   44\n",
       "Healthcare Support                            44\n",
       "Healthcare Practitioners & Technical          41\n",
       "Transportation & Material Moving              35\n",
       "Legal                                         34\n",
       "Architecture & Engineering                    27\n",
       "Personal Care & Service                       27\n",
       "Protective Service                            27\n",
       "Construction & Extraction                     24\n",
       "Life Physical Social Science                  24\n",
       "Installation Maintenance & Repair             18\n",
       "Production Occupations                        18\n",
       "Farming Fishing & Forestry                     9\n",
       "Building & Grounds Cleaning & Maintenance      7\n",
       "Name: occupation, dtype: int64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reviewing the list of occupations to ensure the correct spelling\n",
    "bar_coupons['occupation'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    393\n",
       "0    158\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filtering for a selected criteria \n",
    "\n",
    "filtered_data1 = bar_coupons[(bar_coupons['frequency2'] == '1plus') & #go to bars more than once a month\n",
    "                     (bar_coupons['passanger'] != 'Kid(s)') &         #had passengers that were not a kid\n",
    "                     (bar_coupons['occupation'] != 'Farming Fishing & Forestry')] #occupations other than farming, fishing, or forestry\n",
    "\n",
    "\n",
    "filtered_data1['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6. Compare the acceptance rates between those drivers who:\n",
    "\n",
    "#### - go to bars more than once a month, had passengers that were not a kid, and were not widowed *OR*\n",
    "#### - go to bars more than once a month and are under the age of 30 *OR*\n",
    "#### - go to cheap restaurants more than 4 times a month and income is less than 50K. \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Married partner      882\n",
       "Single               661\n",
       "Unmarried partner    378\n",
       "Divorced              75\n",
       "Widowed               21\n",
       "Name: maritalStatus, dtype: int64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reviewing the list of marital statuses\n",
    "bar_coupons['maritalStatus'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Alone        1200\n",
       "Friend(s)     337\n",
       "Partner       274\n",
       "Kid(s)        206\n",
       "Name: passanger, dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reviewing the list of passanger values\n",
    "bar_coupons['passanger'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    393\n",
       "0    158\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filter:go to bars more than once a month, had passengers that were not a kid, and were not widowed \n",
    "filtered_data2 = bar_coupons[(bar_coupons['frequency2'] == '1plus') & \n",
    "                             (bar_coupons['passanger'] !='Kid(s)') & \n",
    "                             (bar_coupons['maritalStatus'] != 'Widowed')]\n",
    "\n",
    "filtered_data2['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Among all accepted coupons, 48% were accepted by respondents who go to bars more than once a month, had passengers that were not a kid, and were not widowed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    245\n",
       "0     90\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filter on go to bars more than once a month and are under the age of 30 \n",
    "\n",
    "filtered_data3 = bar_coupons[(bar_coupons['frequency2'] == '1plus') & \n",
    "                     (bar_coupons['age'] < '30')]\n",
    "\n",
    "filtered_data3['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Among all accepted coupons, 30% were accepted by respondents who are under the age of 30 and visit bars more than once a month."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "$25000 - $37499     318\n",
       "$100000 or More     291\n",
       "$12500 - $24999     288\n",
       "$37500 - $49999     267\n",
       "$50000 - $62499     262\n",
       "Less than $12500    165\n",
       "$75000 - $87499     151\n",
       "$87500 - $99999     145\n",
       "$62500 - $74999     130\n",
       "Name: income, dtype: int64"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reviewing the income list\n",
    "bar_coupons['income'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\agnek\\AppData\\Local\\Temp\\ipykernel_6292\\3569010994.py:12: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  bar_coupons['frequency3'] = bar_coupons['RestaurantLessThan20'].map(frequency_mapping3)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "      <th>frequency</th>\n",
       "      <th>frequency2</th>\n",
       "      <th>frequency3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Kid(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>less3</td>\n",
       "      <td>less1</td>\n",
       "      <td>4plus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Home</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>6PM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>less3</td>\n",
       "      <td>less1</td>\n",
       "      <td>4plus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Work</td>\n",
       "      <td>Alone</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>55</td>\n",
       "      <td>7AM</td>\n",
       "      <td>Bar</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>less3</td>\n",
       "      <td>less1</td>\n",
       "      <td>4plus</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 28 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        destination passanger weather  temperature  time coupon expiration  \\\n",
       "9   No Urgent Place    Kid(s)   Sunny           80  10AM    Bar         1d   \n",
       "13             Home     Alone   Sunny           55   6PM    Bar         1d   \n",
       "17             Work     Alone   Sunny           55   7AM    Bar         1d   \n",
       "\n",
       "    gender age      maritalStatus  ...  Restaurant20To50 toCoupon_GEQ5min  \\\n",
       "9   Female  21  Unmarried partner  ...               1~3                1   \n",
       "13  Female  21  Unmarried partner  ...               1~3                1   \n",
       "17  Female  21  Unmarried partner  ...               1~3                1   \n",
       "\n",
       "   toCoupon_GEQ15min toCoupon_GEQ25min direction_same direction_opp  Y  \\\n",
       "9                  1                 0              0             1  0   \n",
       "13                 0                 0              1             0  1   \n",
       "17                 1                 1              0             1  0   \n",
       "\n",
       "   frequency frequency2  frequency3  \n",
       "9      less3      less1       4plus  \n",
       "13     less3      less1       4plus  \n",
       "17     less3      less1       4plus  \n",
       "\n",
       "[3 rows x 28 columns]"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Preparing frequency mapping for the variable RestaurantLessThan20\n",
    "\n",
    "frequency_mapping3 = {\n",
    "    'never': 'less4',\n",
    "    'less1': 'less4',\n",
    "    '1~3': 'less4',\n",
    "    '4~8': '4plus',\n",
    "    'gt8': '4plus'\n",
    "}\n",
    "\n",
    "# Use map function to apply the mapping and create the new column\n",
    "bar_coupons['frequency3'] = bar_coupons['RestaurantLessThan20'].map(frequency_mapping3)\n",
    "\n",
    "# Display the updated DataFrame\n",
    "bar_coupons.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    558\n",
       "1    388\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Filtering on go to cheap restaurants more than 4 times a month and income is less than 50K\n",
    "\n",
    "filtered_data4 = bar_coupons[(bar_coupons['frequency3'] == '4plus') & \n",
    "                     (bar_coupons['income'] =='Less than $12500')| \n",
    "                     (bar_coupons['income'] == '$12500 - $24999')|\n",
    "                     (bar_coupons['income'] == '$25000 - $37499')|\n",
    "                     (bar_coupons['income'] == '$37500 - $49999')]      \n",
    "\n",
    "filtered_data4['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Out of all the respondents who accepted bar coupons 47% respondents been to a cheap restaurant 4 times or more and make income of less than 50K. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7.  Based on these observations, what do you hypothesize about drivers who accepted the bar coupons?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Findings Summary\n",
    "\n",
    "Based on the observations above, I hypothesize that drivers who accepted the bar coupons tend to exhibit the following characteristics:\n",
    "\n",
    "#### Younger Age Group:  \n",
    "A significant proportion of coupon acceptance comes from younger respondents, specifically those under the age of 30, with a notable acceptance rate of 59% among those aged 25 or younger who visit bars more than once a month.\n",
    "\n",
    "#### Frequent Bar Visits: \n",
    "Respondents who visit bars more than once a month are more likely to accept coupons, with 48% of all accepted coupons being attributed to this group, particularly if they are under 30.\n",
    "\n",
    "#### Passenger Type: \n",
    "The presence of non-child passengers appears to correlate with higher coupon acceptance rates.\n",
    "\n",
    "#### Marital Status: \n",
    "Respondents who are not widowed are more likely to accept coupons.\n",
    "\n",
    "#### Dining and Income Patterns: \n",
    "A significant portion of coupon acceptors frequently dine at cheap restaurants (4 times or more) and have an annual income of less than $50K.\n",
    "\n",
    "These characteristics suggest that younger, more socially active drivers with lower income levels, who frequently visit bars and inexpensive restaurants, and who often have non-child passengers, are more inclined to accept bar coupons.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Independent Investigation\n",
    "\n",
    "Using the bar coupon example as motivation, you are to explore one of the other coupon groups and try to determine the characteristics of passengers who accept the coupons.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Independent Investigation\n",
    "\n",
    "#### Business Goals: To explore the coffee house coupons and determine the characteristics of passengers who accept the coupons.\n",
    "\n",
    "#### General\n",
    "1.1 How does the coffee house coupon acceptance rate compare to the bar coupon acceptance rate?\n",
    "\n",
    "#### Demographics\n",
    "2.1 How do gender and age affect the acceptance of coffee house coupons?\n",
    "\n",
    "#### Environmental Circumstances\n",
    "3.1 Does destination and time of day affect the accepted coffee house coupon rate?\n",
    "\n",
    "3.2 Do weather conditions and time of day affect coupon acceptance rate?\n",
    "\n",
    "#### Distance & Duration\n",
    "4.1 What is the relationship between direction, coupon duration, & acceptance rate? \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####  1.1 How does the coffee house coupon acceptance rate compare to the bar coupon acceptance rate?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>destination</th>\n",
       "      <th>passanger</th>\n",
       "      <th>weather</th>\n",
       "      <th>temperature</th>\n",
       "      <th>time</th>\n",
       "      <th>coupon</th>\n",
       "      <th>expiration</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>maritalStatus</th>\n",
       "      <th>...</th>\n",
       "      <th>CoffeeHouse</th>\n",
       "      <th>CarryAway</th>\n",
       "      <th>RestaurantLessThan20</th>\n",
       "      <th>Restaurant20To50</th>\n",
       "      <th>toCoupon_GEQ5min</th>\n",
       "      <th>toCoupon_GEQ15min</th>\n",
       "      <th>toCoupon_GEQ25min</th>\n",
       "      <th>direction_same</th>\n",
       "      <th>direction_opp</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>10AM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>2h</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>2h</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>No Urgent Place</td>\n",
       "      <td>Friend(s)</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>80</td>\n",
       "      <td>2PM</td>\n",
       "      <td>Coffee House</td>\n",
       "      <td>1d</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Unmarried partner</td>\n",
       "      <td>...</td>\n",
       "      <td>never</td>\n",
       "      <td>1~3</td>\n",
       "      <td>4~8</td>\n",
       "      <td>1~3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       destination  passanger weather  temperature  time        coupon  \\\n",
       "1  No Urgent Place  Friend(s)   Sunny           80  10AM  Coffee House   \n",
       "3  No Urgent Place  Friend(s)   Sunny           80   2PM  Coffee House   \n",
       "4  No Urgent Place  Friend(s)   Sunny           80   2PM  Coffee House   \n",
       "\n",
       "  expiration  gender age      maritalStatus  ...  CoffeeHouse CarryAway  \\\n",
       "1         2h  Female  21  Unmarried partner  ...        never       1~3   \n",
       "3         2h  Female  21  Unmarried partner  ...        never       1~3   \n",
       "4         1d  Female  21  Unmarried partner  ...        never       1~3   \n",
       "\n",
       "  RestaurantLessThan20 Restaurant20To50 toCoupon_GEQ5min toCoupon_GEQ15min  \\\n",
       "1                  4~8              1~3                1                 0   \n",
       "3                  4~8              1~3                1                 1   \n",
       "4                  4~8              1~3                1                 1   \n",
       "\n",
       "  toCoupon_GEQ25min direction_same direction_opp  Y  \n",
       "1                 0              0             1  0  \n",
       "3                 0              0             1  0  \n",
       "4                 0              0             1  0  \n",
       "\n",
       "[3 rows x 25 columns]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Creating a cofee_house coupon dataset\n",
    "coffee_house = data[data['coupon'] == 'Coffee House']\n",
    "\n",
    "# Reviewing the coffee_house dataset columns\n",
    "coffee_house.head(3)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    2001\n",
       "1    1995\n",
       "Name: Y, dtype: int64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the proportion of accepted/declined coffee house coupons\n",
    "coffee_house['Y'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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i2+//VZs3bpVvPTSS0KtVosZM2aYt8t/LtatW1c89NBDYv369eL7778XDRs2FO7u7uLixYtCCCEuXLgghg0bJgCY/7aRkZHm51hZH9/p06cLAGLChAli06ZNYuHChSIoKEj4+/uLbt26WTwWmZmZwtXV1fxavvv34+PjLbZ9+eWXBQDx559/mi/77rvvhEqlEoMHDxZr1qwR69evFwMHDhQajUZs377dvF3+viQqKqrcv3vs2DHh6uoqQkJCxIIFC8SOHTvE999/L0aMGCFSUlJEXFxcia/pst5OeZ7rBZ06dUrce++9wt/f3+JvJ8Sd11VISIjo16+fWLt2rVi7dq0IDw8Xnp6e4vbt2+br2blzp3B0dBRdu3YVq1atEps3bxbjxo0r9LosyqRJkwQAcebMmRK3y7d7926h1WpFRESEWLVqlVi7dq3o06ePUKlU4ocffhBCCHH16lWxZs0aAUA8++yzIjIyUvz111/iwoUL4ssvvxQAxPvvvy8iIyPFqVOnynUfYmJiRN26dUW9evXEV199JbZv3y5mzZoldDqdGDduXKn58/dtubm5hf7dvHlTABDTp083b1/W946inqtC3Hkd79q1SwghRFpamvD29hbt2rUTP/74o9izZ49YtWqVePrpp8Xp06fNv1fW121BBoNBODs7i3vuuafUxyJf/nPgmWeeEZs3bxYLFiwQvr6+om7duhav53r16omxY8cW+ZjevY8o675LiDv73z59+oi1a9eKVatWiYiICOHo6Cj27t1r3i5//9KkSRPx9ttvi23btonPPvtM6HQ68cQTT5T5vtYUxRSxgwcPitzcXJGamip+++034evrK9zc3MxPorFjxwoAYsmSJRa/v2DBAgFA/PjjjxaXf/TRRwKA2Lp1q/kyAMLJycniiWkwGERYWJho2LCh+bKRI0cKnU4nrly5YnGd/fv3F87OzuadWv4T6L777it0v1avXm3xgrpbwSK2efNmAUDMnj3bYrtVq1ZZlFEh8p7cer1eXL582XxZZmam8PLyEk899VSh27pbeR6r4spVUQrurGJiYsTbb78tAIgFCxZYbFtUEbvnnntEYGCgyMzMNF+WkpIivLy8LN6cIiMjBQDx6aefWlzn1atXhZOTk3jllVcsMgEQO3bssNj2p59+EgDEsWPHynTfCurZs6fQ6/Xm0pb//F28eLF5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\n",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Preparing data for pe charting to illustrate the proportion of accepted and rejected coupons\n",
    "labels = ['Rejected', 'Accepted']\n",
    "sizes = [2001, 1995]\n",
    "\n",
    "# Create the pie chart\n",
    "plt.figure(figsize=(6, 6))\n",
    "plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)\n",
    "\n",
    "# Equal aspect ratio ensures that pie is drawn as a circle\n",
    "plt.axis('equal')\n",
    "\n",
    "# Title of the pie chart\n",
    "plt.title('Proportion of Riders Accepted/Rejected the Coffee House Coupon')\n",
    "\n",
    "# Display the pie chart\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A total of 49.1% of respondents accepted the coffee house coupon. The acceptance rate for coffee house coupons is slightly higher compared to bar coupons, which had an acceptance rate of 41%."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2.1 How does gender and age affect the acceptance of coffee house coupons? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    gender      age  Y  Counts    concatenated\n",
      "0   Female       21  0     183       Female-21\n",
      "1   Female       21  1     224       Female-21\n",
      "2   Female       26  0     196       Female-26\n",
      "3   Female       26  1     220       Female-26\n",
      "4   Female       31  0     186       Female-31\n",
      "5   Female       31  1     179       Female-31\n",
      "6   Female       36  0      93       Female-36\n",
      "7   Female       36  1      82       Female-36\n",
      "8   Female       41  0      96       Female-41\n",
      "9   Female       41  1      89       Female-41\n",
      "10  Female       46  0      63       Female-46\n",
      "11  Female       46  1      48       Female-46\n",
      "12  Female   50plus  0     193   Female-50plus\n",
      "13  Female   50plus  1     139   Female-50plus\n",
      "14  Female  below21  0      31  Female-below21\n",
      "15  Female  below21  1      29  Female-below21\n",
      "16    Male       21  0     237         Male-21\n",
      "17    Male       21  1     239         Male-21\n",
      "18    Male       26  0     213         Male-26\n",
      "19    Male       26  1     214         Male-26\n",
      "20    Male       31  0     140         Male-31\n",
      "21    Male       31  1     118         Male-31\n",
      "22    Male       36  0     121         Male-36\n",
      "23    Male       36  1     106         Male-36\n",
      "24    Male       41  0      66         Male-41\n",
      "25    Male       41  1      74         Male-41\n",
      "26    Male       46  0      44         Male-46\n",
      "27    Male       46  1      65         Male-46\n",
      "28    Male   50plus  0     123     Male-50plus\n",
      "29    Male   50plus  1      90     Male-50plus\n",
      "30    Male  below21  0      16    Male-below21\n",
      "31    Male  below21  1      79    Male-below21\n"
     ]
    }
   ],
   "source": [
    "# Creating counts grouped by gender, age, Y (accepted/rejected)\n",
    "counts1 = coffee_house.groupby(['gender','age','Y']).size().reset_index(name='Counts')\n",
    "counts1['concatenated'] = counts1['gender'].str.cat(counts1['age'], sep='-')\n",
    "\n",
    "# Reviewing the count1 result\n",
    "print(counts1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2EAAAJuCAYAAAA5LQpeAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAACW/0lEQVR4nOzdeXwN9/fH8XMjEYklsUZChMRWhBJKLbXTKKWU6kb6tdVa1FJbraVFLaXoQpXaqpZWLbW2pWittZSixFKJoLZYEknO7w+/O82VhCRi7r3p6/l43AeZO3fmfGbmzr3vOzOfsaiqCgAAAADAFC72LgAAAAAA/ksIYQAAAABgIkIYAAAAAJiIEAYAAAAAJiKEAQAAAICJCGEAAAAAYCJCGAAAAACYiBAGAAAAACYihAEAAACAiQhhQCZ14MAB6dChgwQFBYmHh4d4eHhIiRIlpEuXLrJ792671VW0aFEJCwszbX5XrlyRN998UwoVKiTZs2eXsmXLyogRI9I9vUqVKonFYpGJEydmXJGP4MCBA/LGG29IsWLFJFu2bJIjRw6pVKmSjB8/Xv7555/HNt/z58/LiBEjZP/+/Wl6XVhYmBQtWtRmmMVikR49emRccSIyY8YMmTt3bpLh4eHhYrFYkn3ucVuzZs0jbXsPs3XrVmnTpo0UKlRIsmbNKl5eXlK9enWZOXOm3Lx587HN19E52ns2LR73NgPAfghhQCb0ySefSEhIiPz666/y1ltvyffffy+rV6+W3r17y+HDh6VKlSry119/2btMU7Rv314WLlwoQ4cOle+++046dOgg27dvT9e09u/fL/v27RMRkdmzZ2dkmeny2WefSUhIiOzatUv69+8v69atkxUrVkjr1q1l1qxZ0qFDh8c27/Pnz8vIkSPTHMKGDRsmK1aseDxFJZJSCPP19ZUdO3bIc88999hruN+aNWtk5MiRj2Xaw4cPl2eeeUb+/vtvGT16tGzYsEEWL14s9evXlxEjRsjQoUMfy3wdnaO9Z9PqcW4zAOzL1d4FAMhYv/zyi3Tr1k2ee+45+eabbyRr1qzGc/Xq1ZPu3bvL0qVLxcPDw45VZoz4+HiJi4sTd3f3ZJ+/efOmrF69Wvr37y9du3YVEZH69etL37590zW/zz//XEREnnvuOVm9erVs375dqlevnr7iH9GOHTuka9eu0rBhQ1m5cqXNMmjYsKG8/fbbsm7dOrvUlpxbt26Jp6enBAUF2bUOd3d3qVatml1ryGhLly6VUaNGSYcOHeSzzz4Ti8ViPBcaGioDBgyQHTt22LFC+3Gk9ywA2FAAmUqTJk3Uzc1Nz58/n6bX7dq1S5s1a6a5c+dWd3d3ffLJJ3XJkiU243zxxRcqIrp582Z98803NW/evJonTx594YUX9O+//7YZNzY2Vvv3768+Pj7q4eGhNWrU0F9//VUDAgK0ffv2NuNGRERo586dtVChQurm5qZFixbVESNG6N27d41xTp06pSKiH3zwgY4ePVqLFi2qWbJk0bVr16bYplu3bmmWLFm0RYsWaVoWybl9+7bmzp1bQ0JC9NixYyoi2qFDh2THXblypQYHB2vWrFm1WLFiOmXKFB0+fLjev8tNSEjQjz/+WCtUqKDZsmVTb29vbdWqlf71118Pradp06bq6uqqZ86cSVX98fHx+sEHH2ipUqU0a9asmj9/fn399df17NmzNuPVrl1by5Ytq7/99pvWrFlTPTw8tFixYjpu3DiNj49XVdUtW7aoiCR5DB8+XFVV27dvr9mzZ9cDBw5ow4YNNUeOHFqtWjXjuYCAAJt5ioh2795dZ82apSVKlNCsWbPqE088oYsWLbIZL7llqPrvdnnq1ClVVQ0ICEhSm3We1u3oiy++sJnG1q1btV69epojRw718PDQp59+Wr///vtk55Oa7f9+7du3T3aZWWu+ffu2vvPOO1q0aFF1c3NTPz8/7datm165cuWB01VVLVeunObOnVtv3rz50HHTMq/E6zSx+9/D1uWyfv16DQsL09y5c6unp6c2bdo02W159uzZWr58eXV3d9fcuXNrixYt9I8//rAZx7oNHT9+XENDQzV79uxauHBh7du3r965cyfV7Uzte3bt2rVar149zZUrl3p4eGjp0qV17NixNuPs3LlTmzZtqnny5FF3d3cNDAzUt956y2acY8eO6csvv6z58+fXrFmzaunSpXX69Ok241jfP/Pnz9c+ffqoj4+PZsuWTZ955hndu3evzTJ40DYzffp0rVWrlubPn189PT21XLly+sEHH2hsbKzN/FLznra6cuWK9u3bV4sVK2bsJ0JDQ/XIkSPGODExMTp69GhjX5IvXz4NCwvTqKioVK0XAPcQwoBMJC4uzvgCmRabN2/WrFmzaq1atXTJkiW6bt06DQsLS/Jl1fplKzAwUHv27Kk//PCDfv7555o7d26tW7euzTTbt2+vFotF+/fvr+vXr9dJkyZpoUKFNFeuXDZf4CIiItTf318DAgL0k08+0Y0bN+ro0aPV3d1dw8LCjPGsX54LFSqkdevW1W+++UbXr19vfCFJifWLzLRp09K0TO63YMECFRH9+OOPVVW1Zs2amiNHDr1x44bNeGvXrlUXFxetU6eOrlixQpcuXapVq1bVokWLJgkQnTp1Ujc3N3377bd13bp1unDhQi1durT6+PhoZGRkirXExcWpp6enVq1aNdX1d+7cWUVEe/TooevWrdNZs2Zp/vz51d/fXy9evGiMV7t2bc2bN6+WKFFCZ82apRs2bNBu3bqpiOiXX36pqqrXrl0ztoWhQ4fqjh07dMeOHUaga9++vRGmx40bp5s2bdIffvjBeC65EObv769lypTRRYsW6XfffafPPvusioguXbrUGC+1IWzv3r0aGBioFStWNGqzfrlNLoT9+OOP6ubmpiEhIbpkyRJduXKlNmrUSC0Wiy5evDjJfFKz/d/vxIkT+uKLL6qIGDXt2LFD79y5owkJCdq4cWN1dXXVYcOG6fr163XixImaPXt2rVix4gNDx/nz51VE9KWXXnrg/K3SMq+0hjB/f3/93//+p2vXrtVPP/1UCxQooP7+/jbhbuzYsSoi+vLLL+vq1at13rx5GhgYqF5eXnrs2DFjvPbt2xthfOLEibpx40Z999131WKx6MiRI1PV1tS+Zz///HO1WCxap04dXbhwoW7cuFFnzJih3bp1M8ZZt26durm5afny5XXu3Lm6efNmnTNnjrZt29YY5/Dhw+rl5aXBwcE6b948Xb9+vb799tvq4uKiI0aMMMazhjB/f39t3ry5rlq1Sr/66istXry45sqVywiuD9pmVFX79OmjM2fO1HXr1unmzZt18uTJmi9fPn3jjTds2pea97Sq6vXr17Vs2bKaPXt2HTVqlP7www+6bNkyfeutt3Tz5s2qeu/HnGeffVazZ8+uI0eO1A0bNujnn3+uhQoV0jJlyuitW7dStW4AEMKATCUyMlJFxOaLgVVcXJzevXvXeCQkJBjPlS5dWitWrGhz5En13tEWX19f49dS65etxF9OVFXHjx+vIqIRERGqqnrkyBEVEe3Tp4/NeNYvRYm/wHXp0kVz5Mihp0+fthl34sSJKiJ6+PBhVf33y3NQUFCSX3pTEhERoU8//bSWKlVKLRaLfvLJJ6l6XXLq1aun2bJlM75QWpfF7NmzbcarUqWK+vv7a0xMjDHsxo0bmjdvXpsAsWPHDhUR/fDDD21ef/bsWfXw8NABAwakWMuD1nNyrOvj/vX266+/qojo4MGDjWG1a9dWEdFff/3VZtwyZcpo48aNjb937dqV7BEl1X+D75w5c5J9LrkQ5uHhYRM84+LitHTp0lq8eHFjWGpDmKpq2bJltXbt2knGTS6EVatWTQsUKGDz5TwuLk7LlSunhQsXNt4rqd3+U9K9e/dk61+3bp2KiI4fP95m+JIlS1RE9NNPP01xmjt37lQR0XfeeeeB807PvNIawl544QWb8X755RcVER0zZoyq3jvK4uHhoU2aNLEZ78yZM+ru7q6vvPKKMcy6DX399dc24zZp0kRLlSqVqram5j1748YNzZUrl9asWdNmn3i/oKAgDQoK0tu3b6c4TuPGjbVw4cJ67do1m+E9evTQbNmy6T///KOq/4awSpUq2cwzPDxc3dzctGPHjsawlLaZ+8XHx+vdu3d13rx5miVLFmNeqql/T48aNUpFRDds2JDifBYtWqQiosuWLbMZbt0fzJgx46G1AriHjjmA/4iQkBBxc3MzHh9++KGIiJw4cUKOHj0qr776qoiIxMXFGY8mTZpIRESE/PnnnzbTev75523+Ll++vIiInD59WkREtmzZIiJiTNOqTZs24upqeynq999/L3Xr1hU/Pz+beYeGhoqIyE8//ZRk3m5ubg9t7927dyU0NFQKFCgghw8flk6dOsmbb75pXCMiIrJt2zaxWCxGvSk5deqUbNmyRVq2bCne3t4iItK6dWvJmTOnzJkzxxjv5s2bsnv3bmnRooXNtXg5cuSQZs2aJWm3xWKR1157zabdBQsWlAoVKsiPP/740DamlrV99/dK+dRTT8kTTzwhmzZtshlesGBBeeqpp2yGlS9f3li/qdWqVatUj1u/fn3x8fEx/s6SJYu89NJLcuLECTl37lya5psWN2/elF9//VVefPFFyZEjh838X3/9dTl37lyat/+02rx5s4gkXT+tW7eW7NmzJ1k/j+Jxzuv+93v16tUlICDA2P527Nght2/fTjJvf39/qVevXpJ5WyyWJO+b1G6HqX3Pbt++Xa5fvy7dunWz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EuvVq5dmyZJFhw0bpuvWrdMTJ05ow4YNtX79+jZfPhztegCrvXv3asmSJfWpp54yftWdNWuWli1bVmvUqKEvvfSStm3bNs0dqCR3yuKGDRts7pezZ88etVgsWq9ePd2zZ4+xvMaPH6958uRJco81szl7G6ifbehROXv96fXJJ5+oxWJJtlv53377TWvUqKG+vr66detWPXv2rEZHR2u9evX01VdftUO1qWNdL5cuXdL3339fy5Ytq2+99ZbxfKdOndTDw0MHDhyoEyZM0Lfeektz5sz5yJ0vZSRCWAaJj4/XWbNmGTct/euvvzQwMFDfeOMNff3117VAgQI6ceJE47Sd9P76+rhQv/05exucvX7VzNGGB5kzZ466uroaN9+8cOGCHjx4UNetW6d///23Md6ECRO0SpUq6unpqcHBwVq1alXj1JPHcf1URtu3b58GBQVplSpVjLrXrl2r77//vjZq1Eh79OiRpt7MrG0+deqUfvvtt6p677Sd3r176/Dhw1VV9eTJkxoYGKhhYWEaGBio1apV0927dxuvtff1gs7eBupnG3pUzl5/es2ePVtdXV2NNl+9elWvXLlic13XyZMntU2bNpo9e3YtUqSIlitXToODg439p6Mf/btw4YJ+8MEH+sQTT9gEsTFjxmjjxo21XLly+uyzzzpcx1mEsAx08uRJPXLkiN66dUvr1q2r//vf/1T13kXgBQoU0MDAQP3www81ISHBITdo6rc/Z2+Ds9evmjnakJwzZ85o8eLFtVy5cqp674tIpUqVtEyZMmqxWPSpp57Sd9991xj/7Nmz+vvvv+u+ffuMLyCO1g194nv4fP/997p69Wr966+/VFX1999/1xIlSmiVKlVsrnOIj49PV5D8+++/NV++fPrEE08YXTqvX79eDx8+rFeuXNEqVapox44dVfXeUVKLxaIhISEO9aHv7G2gfvtz9jY4e/1ptWvXLvX09NTXXntNVVVPnDihoaGhWrp0aXV3d9eXX37ZprfAdevW6ZIlS3TJkiXG2Q6Out8/c+aMHjt2zDg18ubNmzp+/PgkQezKlSt68+ZNjY6Otke5D+QqSBdVFYvFYvwrIhIQECAuLi5y4MABiYqKknHjxomIyLlz56RKlSpSuHBhadWqlTG+PVG//Tl7G5y9fpHM0YbUypMnj4wcOVLeffddqVevnkRGRkrTpk2l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\n",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Preparing seaborn barplot\n",
    "plt.figure(figsize=(10, 6))\n",
    "\n",
    "sns.barplot(x='concatenated',y='Counts',hue='Y',data=counts1)\n",
    "\n",
    "# Add labels and title\n",
    "plt.xlabel('Gender & Age')\n",
    "plt.ylabel('Counts')\n",
    "plt.title('Gender & Age Contribution to Coupon Acceptance')\n",
    "plt.xticks(rotation=45)\n",
    "\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3.1 Does destination and time of day affect the accepted coffee house coupon rate?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No Urgent Place    2155\n",
       "Home                928\n",
       "Work                913\n",
       "Name: destination, dtype: int64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Creating value counts to preview the distribution of the destination column\n",
    "coffee_house['destination'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        destination  time  Y  Counts          concatenated\n",
      "5   No Urgent Place  10AM  1     576  10AM-No Urgent Place\n",
      "12             Work   7AM  0     506              7AM-Work\n",
      "2              Home   6PM  0     454              6PM-Home\n",
      "9   No Urgent Place   2PM  1     435   2PM-No Urgent Place\n",
      "13             Work   7AM  1     407              7AM-Work\n",
      "8   No Urgent Place   2PM  0     359   2PM-No Urgent Place\n",
      "4   No Urgent Place  10AM  0     323  10AM-No Urgent Place\n",
      "3              Home   6PM  1     281              6PM-Home\n",
      "10  No Urgent Place   6PM  0     188   6PM-No Urgent Place\n",
      "11  No Urgent Place   6PM  1     170   6PM-No Urgent Place\n",
      "0              Home  10PM  0     138             10PM-Home\n",
      "7   No Urgent Place  10PM  1      71  10PM-No Urgent Place\n",
      "1              Home  10PM  1      55             10PM-Home\n",
      "6   No Urgent Place  10PM  0      33  10PM-No Urgent Place\n"
     ]
    }
   ],
   "source": [
    "# Preparing data for the bar chart based on destination,time of the day, and acceptance rate\n",
    "\n",
    "counts1 = coffee_house.groupby(['destination','time','Y']).size().reset_index(name='Counts')\n",
    "sorted_counts = counts1.sort_values(by='Counts', ascending=False)\n",
    "sorted_counts['concatenated'] = sorted_counts['time'].str.cat(sorted_counts['destination'], sep='-')\n",
    "\n",
    "print(sorted_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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nE/qoXJxccHly5fh7++PP//8EyICd3d3jk5OREREOdJH9VAdP34c7u7uiIyMBAA0bNgQgwcPxpAhQ1C5cmWULl0ap0+fTpdCiYiIiDKrjwpUCxcuRO/evWFlZZVinrW1Nfr27Yv58+enWXFEREREWcFHBaqrV6/i888/f+/8Ro0aITAwUOeiiIiIiLKSjwpUT548SXW4hCRGRkZ4+vSpzkURERERZSUfFagKFCiA69fff6n0tWvX4OjoqHNRRERERFnJRwWqpk2bYtKkSYiJiUkxLzo6GpMnT4a3t3eaFUdERESUFXzUsAkTJkzAzz//jOLFi2PQoEEoUaIEFEXBH3/8gSVLliAxMRHjx49Pr1qJiIiIMqWPClT29vY4e/Ys+vfvj7Fjx0JEAACKoqBx48ZYunQp7O3t06VQIiIioszqowf2LFSoEA4cOIDw8HD89ddfEBG4ubnBxsYmPeojIiIiyvQ+aaR0ALCxsUHlypXTshYiIiKiLOmT7uVHRERERP/DQEVERESkIwYqIiIiIh0xUBERERHpiIGKiIiISEcMVEREREQ6YqAiIiIi0hEDFREREZGOGKiIiIiIdMRARURERKQjBioiIiIiHTFQEREREemIgYqIiIhIRwxURERERDpioCIiIiLSEQMVERERkY4YqIiIiIh0xEBFREREpCMGKiIiIiIdMVARERER6YiBioiIiEhHDFREREREOmKgIiIiItIRAxURERGRjhioiIiIiHTEQEVERESkIwYqIiIiIh0xUBERERHpiIGKiIiISEcMVEREREQ6YqAiIiIi0hEDFREREZGO9BqoZs6cicqVK8PS0hL58+dHq1atcOvWLa1lRAQ+Pj5wcnJCrly5ULduXdy8eVNrmdjYWAwePBh58+ZF7ty50aJFCzx48CAjPwoRERHlYHoNVAEBARg4cCDOnz8Pf39/JCQkoFGjRnjz5o26zOzZszF//nwsXrwYFy9ehIODAxo2bIhXr16pywwbNgy7du3C1q1bcebMGbx+/Rre3t5ITEzUx8ciIiKiHMZInys/dOiQ1vN169Yhf/78CAwMxGeffQYRwcKFCzF+/Hi0adMGAODn5wd7e3ts3rwZffv2RUREBNasWYMNGzagQYMGAICNGzfCxcUFR48eRePGjTP8cxEREVHOkqnOoYqIiAAA2NraAgCCg4MRGhqKRo0a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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Preparing seaborn barplot\n",
    "sns.barplot(x='concatenated',y='Counts',hue='Y', data=sorted_counts)\n",
    "\n",
    "# Add labels and title\n",
    "plt.xlabel('Destination')\n",
    "plt.ylabel('Counts')\n",
    "plt.title('Coupons by Destination')\n",
    "plt.xticks(rotation=45)\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Overall, a higher number of drivers were presented with the coffee house coupon while en route to non-urgent destinations. Drivers are more likely to accept the coupon when driving to non-urgent places and more likely to reject it when driving to work or home. Among all accepted coffee house coupons, 63% were by drivers heading to non-urgent destinations.\n",
    "\n",
    "Upon analyzing the data based on destination and time of day, it is evident that drivers exhibit a higher likelihood of accepting the coffee house coupon when en route to non-urgent destinations at 10 a.m. and 2 p.m. Conversely, they are less inclined to accept the coupon during their morning commute to work or at 6 p.m.commute back home."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3.2 Do weather conditions and time of day affect coupon acceptance rate?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    time weather  Y  Counts\n",
      "18   6PM   Sunny  0     571\n",
      "3   10AM   Sunny  1     513\n",
      "22   7AM   Sunny  0     482\n",
      "13   2PM   Sunny  1     420\n",
      "19   6PM   Sunny  1     396\n",
      "23   7AM   Sunny  1     346\n",
      "12   2PM   Sunny  0     342\n",
      "2   10AM   Sunny  0     293\n",
      "9   10PM   Sunny  1      71\n",
      "6   10PM   Snowy  0      70\n",
      "4   10PM   Rainy  0      68\n",
      "1   10AM   Rainy  1      63\n",
      "21   7AM   Snowy  1      61\n",
      "16   6PM   Snowy  0      61\n",
      "17   6PM   Snowy  1      40\n",
      "5   10PM   Rainy  1      40\n",
      "8   10PM   Sunny  0      33\n",
      "0   10AM   Rainy  0      30\n",
      "20   7AM   Snowy  0      24\n",
      "10   2PM   Snowy  0      17\n",
      "7   10PM   Snowy  1      15\n",
      "11   2PM   Snowy  1      15\n",
      "15   6PM   Rainy  1      15\n",
      "14   6PM   Rainy  0      10\n"
     ]
    }
   ],
   "source": [
    "# Grouping by time of the day and the weather\n",
    "counts2 = coffee_house.groupby(['time','weather','Y']).size().reset_index(name='Counts')\n",
    "\n",
    "sorted_filtered_df = counts2.sort_values(by='Counts', ascending=False)\n",
    "\n",
    "# Review the summary result\n",
    "print(sorted_filtered_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatinate two string columns for clear charting\n",
    "sorted_filtered_df['concatenated'] = sorted_filtered_df['time'].str.cat(sorted_filtered_df['weather'], sep='-')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>time</th>\n",
       "      <th>weather</th>\n",
       "      <th>Y</th>\n",
       "      <th>Counts</th>\n",
       "      <th>concatenated</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>6PM</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>0</td>\n",
       "      <td>571</td>\n",
       "      <td>6PM-Sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10AM</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>1</td>\n",
       "      <td>513</td>\n",
       "      <td>10AM-Sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>7AM</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>0</td>\n",
       "      <td>482</td>\n",
       "      <td>7AM-Sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2PM</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>1</td>\n",
       "      <td>420</td>\n",
       "      <td>2PM-Sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>6PM</td>\n",
       "      <td>Sunny</td>\n",
       "      <td>1</td>\n",
       "      <td>396</td>\n",
       "      <td>6PM-Sunny</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    time weather  Y  Counts concatenated\n",
       "18   6PM   Sunny  0     571    6PM-Sunny\n",
       "3   10AM   Sunny  1     513   10AM-Sunny\n",
       "22   7AM   Sunny  0     482    7AM-Sunny\n",
       "13   2PM   Sunny  1     420    2PM-Sunny\n",
       "19   6PM   Sunny  1     396    6PM-Sunny"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted_filtered_df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkYAAAH/CAYAAACy8BJMAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB8tUlEQVR4nO3dd3xN9/8H8NfJHiLEyCD2FjtWjIQQK3aN8rOqKEURo3aMUptSe1Ozqlo7iFV71ajaakbMJCIy378/3Hu+uRkEyR28no9HHo/cM+5933POPed1PmcpIiIgIiIiIpgZugAiIiIiY8FgRERERKTBYERERESkwWBEREREpMFgRERERKTBYERERESkwWBEREREpMFgRERERKTBYERERESkwWBkxM6fP48uXbogf/78sLGxQaZMmVC+fHlMnjwZz549M3R5RkdRFPTu3TvD3t/HxweKorzzLzAwUC/1BAYGpqkeHx8f3L59G4qiYPny5RlWT0aaPXs2ChUqBCsrKyiKghcvXqQ43PLly3W+u42NDVxcXFCrVi1MnDgRoaGh+i08icuXL6NRo0ZwcnJClixZULVqVWzcuDFN48bHxyNLlixo0KBBsn4zZsyAoij48ssvk/UbN24cFEXB+fPnP7r+pF69eoXAwEDs378/WT/t8vnkyZN0/9z3dejQIbRu3Rq5cuWClZUVHB0d4eXlhXnz5iEyMlLv9WiX09u3b6vdfHx84OPjo75+27RNaXxKPxaGLoBStmjRIvTq1QtFixbFoEGDUKJECcTGxuLUqVOYP38+jh49is2bNxu6zM/K3LlzER4err7etm0bxo8fj2XLlqFYsWJq99y5c+ulnq+//hr169dXXz98+BAtWrRAnz590K5dO7V75syZ4erqiqNHj6JgwYJ6qS09nTt3Dn379sXXX3+NTp06wcLCAg4ODm8dRztPYmNjERoaisOHD2PSpEmYOnUq1q9fjzp16uip+v8JDw9H3bp14eDggIULF8LOzg4HDx7E0aNH0apVq3eOb25ujho1amD//v2Ii4uDhcX/Vt/79++Hvb09goODk423f/9+ZMuWDaVKlUrX7wO82XiPGTMGAHQ26sZk9OjRGDt2LLy8vDBu3DgULFgQr169wpEjRxAYGIirV69ixowZhi4Tc+fO1Xn9tmnbqFEjHD16FK6urvoq7/MiZHSOHDki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51izZg0Aw+84GnOdidfR2v8TEhLQoEEDXLt2DeHh4QA+bj4zGJmAKVOmwNvbGwsWLEBUVBQAoFy5cggLC1P3KI1hha6lXVivXLmi87pixYrInTu3unHXd0uCqYQOU5rfSQOHdp72798frq6u+Pnnnw1RVjLaZfDatWuIiIhQu48dOxavX79WWzwMsaJPOi+107BWrVpwcXHByZMndbobinYaagOGlZUVAKBSpUq4fPky9u3bZ7DaAOPemGtpP3vNmjWYOXOm2t3JyQljxozBli1b1OlrSMZe58KFC1GkSBFs2bIFN27cgJmZGbp06YLbt29jypQpAD5uPjMYGaGkP3BfX184Oztj+fLlKFasGObNmwdbW1uMGDECkyZNwp07dwy+h5HU3r17UaJECXTs2BFz584FAHh4eMDb2xujRo1CbGysQVoSjDF0mPL81m58lixZorO3ZmdnB09PT+zevVsd1tDN7r///jtq1qyJ5s2bIzg4GE+ePIGdnR1atmyJM2fOIC4uTu/1Af9bga9evRp//fWX+rsoWbIkSpQogQkTJgAwjsNAu3btQp06deDn54fffvsNz58/h4eHB/r374+ffvoJt27dMlhtxr4x14qJicGGDRvw008/wcPDA3PmzMGVK1fg5+cHJycn9YIAQwdhY6pTu+4QEcTHx6NYsWIoX748xo4diyZNmmDGjBl4+fIlfvjhB1y4cAE3btz46A8kIxIfH6/+HxMTI69evRIRkdjYWLl//74MGzZMvL29JXfu3NK0aVPJnz+/bNy4UURE4uLiDFKziG7dIm/q3blzp3z99ddSoEABKV++vCxatEgOHz4s9evXl6VLl4qISEJCQobWlfT9T58+LV988YVUqVJF8uTJI3PnzpWQkBBZvny55M6dW/77778MrScpU53fiT18+FA8PDwkT5484u/vL5s2bVK7u7i4yKJFiwxcociuXbtERGTz5s3SrVs3yZo1qzRt2lSWLl0qR44cEXNzc9m2bZvB6rt8+bLUrVtXFEWRHj16yIIFC0RE5MaNG1KtWjVZtmyZQepK+ru+f/++nDt3Tvz9/aVatWpSoEABWbdunSxYsEDq168vQUFBImK4ZTM6Olr9nZQsWVJmz54t//77rzx9+lQqVaqkrncMVd/UqVPlp59+EhGRiIgI6d27t9SrV0+yZMkiixcvlmrVqknx4sUlPDzcIPUZY52Jl8HIyEidfsePH5dZs2ZJ3rx5xdfXV0qUKCG5c+dWf8sfun1hMDJSEyZMkPr164ufn5+6odH677//ZMuWLVK1alWxs7MTLy8vA1X5RuIF999//5V79+6pP5jw8HB5+vSpfPPNN1K/fn2xt7cXKysradu2rV7rMvbQYarzO7F169ZJ//79xdraWlq2bCljxoyRvn37SpcuXSQ6OjrV8TLaxYsXpUiRIrJixQq12969e2XcuHGSNWtWady4sVhbW0vz5s0lIiIiw8O6SOrTcOvWrfL111+Lq6ur+Pr6ypQpU6R69erSr1+/DK8pqcQ1Xrp0Se7fvy/Pnz9X+128eFEGDx4snp6eUqNGDVEURerXr6/3OrWMaWOulXhZio6Olh9++EGqVasmp06dUrs/fvxY5s+fL7Vr15aSJUuKoijyyy+/iEjqy8nnWOekSZPEx8dH2rZtK/PmzdPpd/PmTdm4caM0aNBAFEWRChUqyOPHjz/4sxiMjETiBWvChAmSI0cOGTBggLRs2VIURZGZM2cmG+fFixeyfft28fDwUDfohjRs2DDJnTu3FC5cWGrVqiX37t3T6R8aGirLly+X2rVri4ODg/z66696qcsYQ4epzu/EdW/ZskU2btwoW7du1RnmxIkTMmbMGClVqpQoiiLm5uZy9uxZvdWYNNQ+f/5cOnToIE2bNpWwsDCdfk+ePJGJEydK/fr1xdbWVq5fvy4iGduSmfi9//zzT1mxYoUcOXJEXr9+LSJvNuoPHjyQzp07S9u2bUVRFFEURW310rfvv/9eChYsKM7OztK5c2cJDg7W6f/333/Ln3/+KdWrVxd3d3fZsWOHiOi3NdgYN+Ypvf+pU6ekatWqMm7cuGTf4f79+3LmzBmpVKmS1K5dO0NrM4U6E9c1bdo0cXJyku+//14aNWokxYoVkyFDhqQ43vLly6VixYpy8uTJZLWnFYORkbl69apMmzZN9u7dKyJvWjpmzJghZmZmMmPGDHU47UITFhYm1atXl8DAQL3XmnjB3blzp7i6usqff/4pc+fOlTp16oiLi4vcvXs32bC3b9+WL7/8Ul2w03sFakqhw5Tmd+L5NGDAAHFycpL8+fNLrly5pHfv3smGjYmJkZ9//lm8vLykffv26oZfX3bu3KkGndu3b4ujo6POdIuJiVFrFRGpU6eOtG/fXm+haMCAAeLs7CzOzs5SunRp6dOnj86hgvj4eHn27JksXrxYSpcuLQMHDlS7Z2R9iWvcvn27uLu7y86dO2Xq1KnSuHFjqVatmuzZsyfZuM+fPxcvLy/p27dvhtWnZawb85RMnDhR2rZtq4byX375RczNzeXEiRMikjzI37x5U1xcXJIF0M+pzsSf9ddff8kPP/yg7hg8evRIpkyZInnz5tUJR4nXL2XLlpVvv/32gz+fwciI7NmzRxRFkZw5c8q+fft0+s2YMUPMzc11NuraH37Tpk2lXbt2EhcXp5fDAEktXbpUfv75Z/n555/Vbv/884/Url1bnJ2d1XAUHR2t9p8yZYoUK1ZMXr58mWF1GXvoMNX5/eDBA6lataqcP39erl69KitWrBB7e3vp2rWrOkzildSCBQukdOnS8vTpU73V+Ouvv4qiKJI/f375888/ReTNob7ChQurLRpa2mk4adIk8ff3z5B6EhISdDbm586dE19fXzlz5ow8ePBAJk6cKFWqVJEuXbqoh3wTD79w4ULJmjXrRx0eeF9btmyRvn37yqxZs9RuwcHB0rJlS6latapOONL+thctWiSlS5eWZ8+e6aVGY9qYJ5WQkCCvXr2SXLlyiaIoUqtWLVm6dKncvXtXBg8eLF5eXvLgwYNk4zx9+lSKFSsmu3fvzvAaja3Or7/+Wmc7sW/fPnF1dRVXV9dkLYHTpk2TfPnyyffff692187v1q1bS+/evT/4lAgGIyPy9OlTGTVqlFhaWqonXybe8M2aNUsURZH169er3Q4ePCiFChWSv//+W+/1irw5FOXh4SGKosjkyZN1+l2+fFl8fX3Fzc1Nbt++LSL/+z5DhgyRcuXKJTu0kV5MIXSY4vyeNm2aNGzYUD1vSEQkKipK1q5dK/b29tKtWzd1WG2LTGhoqLi4uMj+/fszrK6kLQgRERFSp04dKV68uBQpUkSGDh0q06dPl549e0pAQIA8efIk2Xv06NFDihYtKhEREela27///qvzeu3ateLv7y+dOnVS6379+rXMnDlTKleuLF999ZUajrTTMCQkREqUKCHHjx9P19q02rZtKwsXLlRfX7x4USpXrixZsmSRCRMm6AwbHBwsX3zxhVSvXj3ZCevt27eXypUrJztJNr0Z08Y86WcktW/fPmnQoIE0a9ZMevToIQ0aNJBvv/1WWrVqleKFCb/88osoiiI3btzIkBqNtc5Tp05J69at1WVe5M25bQEBAeLg4KC2BGo9fvxYZsyYIdbW1upOeUJCghw5ckSsra0/ah3JYGQgiVfkif9/8eKFBAQEiLm5eYrn4Kxfv15iY2PV169fv5aHDx9mbLGJJP1BxcXFSVBQkFSvXl0KFiyYLOj8+++/Urp0aXVPPD4+Xh4/fix+fn5y+vTpDKvT2EKHqc7vxF69eiU//PCD5MiRQ6pWrarT7/Xr17Ju3TrJnDmztGzZUqef9vwAbcthRkp8XtucOXNk+PDhsnbtWhk5cqR6Im6hQoXkwIEDOuPdv39f2rdvr7NXmh4GDx6sXmgQFxcnUVFR0rNnT8mdO7d4enrqDKsNR15eXtK8eXOdVrdhw4aJoijJNvbpITQ0VObMmaOzQRIR2bBhg1SpUkU8PDySTZcDBw5IrVq1pEePHiLyZpmOj4+XmjVrytGjR9O9RhHj3JinZs6cOXLkyBF5/vy5REZGyoABA2TKlCly5swZmT9/vmTKlEkURZFChQqpJ7RrnTlzJlmY/hzqjI+PV+fxkiVL1HB948YNCQgIkIIFC+q09Iu8Oay2du3aZC1DH7uOZDAygMQ/8Pnz50tAQIAMGzZM3YuNioqSAQMGiJmZmXq+S9KVQmxsrN6v8kn8eREREeoPJS4uTg4ePCjly5eXsmXLJgtH//33X7Jao6KiMqQuYwwdn8L81nrw4IHMnDlTLCwsZMSIETr9Xr9+LUuXLhVfX1+dldyCBQv00sK1Y8cOURRFJk6cKFevXpUXL16Il5eXTJs2TUREzp8/r14S36pVq2Tja1tp0tPx48fVZez+/fsiIvLs2TMZMWKEeo5E4pX669evZfz48dKtWzed6b9161b1ZNKMNHfuXBk8eLD6euPGjVK7dm1p0qSJnDlzRmfYs2fPqjXq8ypOY9qYp6Z69epSvHhx+fbbb+X69ety4sQJKVy4sLozePr0aWnWrJl4e3sb7GpNY63z1q1bkjdvXilXrpz6m7x69aoMGjRIihYtmuI5oiJvlsH0qpHBSM8Sb/BGjx4t9vb28sUXX4i9vb1UrFhRDh48KAkJCRIVFSUBAQFiZWUlK1euNGDFyQUGBkr16tWlRIkSMnfuXLX7wYMHpWLFilK+fPkUD5ElXnmm12EqYw8dpjq/E0+Pv//+W06cOKG2KDx//lymTZsmjo6OMmrUKJ3xErc6JA6dGUE7bRNP49mzZ0vFihWlTp06snbtWrlw4YJkz55dvb9OfHy8rF69Wu+3Y1i/fr3kz59fjh07JiJvwtHgwYOlcuXKMnz48GS3ltB+J32eRxYRESH9+/eXggUL6hy2WLt2rfj6+kqTJk1SvLowce36qNXYNuapfcbixYulZcuW4uTkJNu2bZMuXbpI+fLl1fPEnj59qjOfWaeon7F7927x9PSUihUrquHoypUrMnjwYClRokSyw2rpjcHIQG7fvi0tWrRQzxmIioqScuXKiaenpxw4cEASEhLk9evX0rVrV6levbpBa038g5o5c6a4uLjIDz/8IL179xZzc3MZMGCAuvAePHhQqlSpIrly5dLLeQZaxh46TGl+JzZkyBDJkSOHODs7S+HChdX6X7x4IdOmTZOsWbMa/IrIZ8+eSWRkpLo8nDx5UsaNGycODg7Spk0bady4sXTu3DlZa2BGB7fEduzYIY0aNZJKlSqp0/Dp06cyaNAgqVKliowcOTLZhkvfNz8VedO6O3r0aClWrJiMGTNG7b527Vrx8/OTatWqydWrVzO0rsSMfWOeuL6goCDZsmWLzuH5p0+fyrRp0yRbtmzSqFEjyZYtm8yYMUNnB0Lf980ypjpTm78xMTESFBQk5cqV0wlHV69ele7du0vbtm0zdLoxGBnA9OnTpVChQlKzZk2d8y7Cw8OlfPnyOhvLxHuPhnb+/Hn58ccfde5b8+uvv4q5ubn069dPPTwWFBQkXbt21dteubGHDlOa30lvwVCoUCHZtWuXHD58WJo1aybZsmVTT1x98eKFzJgxQxRFkcWLF+utxsTTZ8KECeLl5SXlypWTOnXqyD///KP2++eff6RmzZqSPXt2URQlQ0/+Tiy1lX1QUJA0adJEKlSooBOOhgwZIgUKFFDPhdN3jWFhYRITE6MGxVu3bsnIkSOThaOlS5dK37599XZIxVg35ikJCAgQV1dXKVy4sGTKlEmqVasmBw8eVNeBR44ckR49eoiiKNKuXTu91GTsdSaev6tWrZIhQ4bI0KFD5fDhwyKiG44qVaqkhqM7d+6k2FqcnhiM9CDpiuTOnTuSN29esbS0lIMHD4rI/2ZwRESEVKxYUfLkyaPTbG3I49AiIseOHRNFUcTW1lY2bNig02/Tpk1iYWGh03KkldHhyBhDx6cwvxcvXiyzZs2SH3/8Uad7q1atxMnJST009ezZM1m7dq1eW1+0Ro0aJdmyZZOff/5Zpk+fLj4+PuLk5CQ7d+5Uh3n16pUsWLBAvvrqK70frrhw4YKcP39eLl++rHbbvXu3NG3aVMqXL68eVnvy5InMnTtXbzsSSW+c5+fnJzVq1JBevXqpl9lrw1Hx4sVl7Nixb32PjGZMG/OULF26VHLkyCFnzpyRhw8fyv3796VChQpSsWJFnfOyXrx4IceOHTPY40iMtc7BgweLu7u7NGnSRNq0aSO2trbyxx9/iMibcLRnzx7x9PSUfPny6VzKzxajT8ShQ4fk1q1bIvLmrHk3NzepUaOGzl6uyJs9uC5duhjVs89E3pzDY2FhIUOHDk1W2+bNm0VRFJ17nuijLmMOHaY0v5PeRbhMmTLqc7uSatWqleTMmVO9P5CWPsPRw4cPpVSpUupdjLXatWsnOXLkkEePHqndEn+3jKwx8eeMGDFCSpUqJTlz5pTq1avLxIkT1X67d++WZs2aqYd7E9PnMvD9999Lzpw5Zc6cOTJ9+nQpXbq0VKtWTT0/7/bt2zJ69GjJmjWrLFmyRG91JWasG/PEhgwZIs2aNROR/y1fkZGRUrRoUWnRokWK47DONxYtWiTu7u5qC+ratWvVO72vXr1aRN6Eo61bt0rnzp31Nt0YjPTk4MGD4uzsLKNGjZI7d+6IyJtLi52dncXHx0dnrzIxQz8odOnSpbJ79261jpkzZ4qiKDqXTWo3CPv379fbxtHYQ4epzm/tSfMvXrwQf39/yZUrl5w7d05EdDf8vr6+0qBBA4PUKPLmRn3Zs2dXD49p9yTj4+OlZMmSMnz4cPW1vo0ZM0Zy5Mghe/fulWvXrknXrl1FURS1JhFRb3HRpUsXEdHfIR+tzZs3S8mSJdVWqy1btkimTJkkd+7cUqpUKfVmnNevX5dFixYZbLk0xo25lnbZ6tSpk9SsWVPtrm01//PPP8XFxUVu375t0BZgY6wzPj5eIiIiZNiwYer9s/7880/JnDmzzJgxQz1/9ffffxcR3Xmqj/nLYKRHw4cPFw8PDxkzZoz6FPd79+6pD4w8f/68gSvUFRMTI/nz55eyZcvK/v371QVSe17J9OnTUxwvo8ORqYQOU5vfU6ZMkW7duqk34wwPD5caNWpIwYIF5eLFiyKiuwE3xAMuEytXrpx06NBBfR0bGysxMTHi6+srgwYN0kttSZ06dUqqVaum3lR0586d4uDgIK1atRIHBwcZPXq0OuyJEyf0vsHUTsutW7eqj1PYunWrZMuWTebMmSM7d+6UzJkzi5eXl4SGhuqMq8/fj7FuzFMSHBwsdnZ26gNstTZv3iweHh56vVu5iPHW+fr162Q3T718+bJcv35drl+/LkWLFlWPOOzcuVNtOUp6p3p9YDDKAEkPSyQ2atQo9aRG7Tkx9+7dE0VRkj1vSt9S2gBFRERIpUqVxNPTU4KDg3VajiwtLXVOztQnYwodpjq/k1q6dKnY2NhIQECAOk3Dw8OlevXqUqhQIbl06VKycfT5IM67d+9KSEiI+nrhwoVSvnx5nfspJSQkiJeXl8GWy5cvX8qPP/4o4eHhsm/fPnFxcZGFCxdKeHi41K9fXxRFkT59+uiMk9HT8NatW3Lt2jX1uXFaDx48kFevXom3t7d6HtGLFy+kbNmyYmVlJV9++aWI6P+qqcQMvTHXSjwNfvvtN5kxY4YcPnxYnjx5IgkJCTJs2DDJly+fTJ48WcLCwuS///4Tf39/qV+/vl5bA421zk2bNkmzZs2kVKlS0rt372SPB9q+fbtUqlRJPYx79OhR6dGjhyxfvtwg5y8yGGWgefPmycyZM5Pd02fkyJHi7Oyss7EMDQ01+GEUraSPS9CeyFy+fHnZv3+/uhIbN26cVK9eXW8P3TT20GFK8zu1DdHatWvFwcFB+vfvrxOOvL29JVOmTHLz5k19lqkaNmyYlC1bVrJlyyYjR46UGzduSFRUlHppeZUqVeS7774TLy8vKVGihF5WpkePHpXVq1fLzJkzU7x/0zfffCO9e/dWl9vvvvtOfHx8pEmTJnpr5Vi1apWUKVNG8ubNK1myZJF169bp9L927ZrkypVLvRP4gwcPpE2bNrJ3716DtAga08Y8pfoGDRok2bJlk0KFCombm5v06dNH7t69Ky9evJDx48eLvb29uLi4SKFChcTT01NdLvQxLY21zvnz54ujo6MMGDBA+vbtKzY2NjrPVRT53zmqhw4dkkePHknjxo2lU6dOan99hyMGo3R09epVnbuqtm7dWvLlyyeLFi1KtrFs3ry55MmTRwICAnTur2KIjWXS+xSVLVs22bk6ERERUrx4calQoYLs27dPXVAz+rJJLWMMHaY6vxM7evSovHjxQqfbL7/8InZ2dvLdd9+phyrDwsKkZ8+eBrlyasWKFZIrVy5ZuXKljBs3TvLkySPt27eXf//9V72kt1WrVtKmTRvp06ePumxmZK1LliyRPHnySKlSpcTBwUHKlCmj80DkmJgYqVKlirpyf/XqlXzxxReyatUqdZiM/s3Mnz9frKysZPHixbJhwwZp3ry5KIqi83iPFy9eSMWKFaVBgwaye/duqVOnjtStW1dvd7Q21o15SvWdOHFCGjRoIMePH5f4+HiZPXu2VK5cWbp06aLuRNy5c0c2b94se/fuVaedPjbqxlrnokWLxNraWjZv3qx+hvZec1euXFGHCw8Pl3bt2ql3LC9VqpQ6fw1x+xIGo3Sydu1aqV69ugwaNEhd+EREunfvLoUKFZIFCxbobIACAgKkRIkS0rlzZ4Pet+bYsWOyefNm9Sqeu3fvSvbs2cXX11cNR9oVz86dO8XMzExKlCih85yzjKjf2EOHqc7vxBtv7S0YJk6cmGyarlixQszMzGTYsGFy7do1nX76DHPHjh2TgQMHqleoiIhs27ZNSpYsKe3atVNPDE8qIzdG2qszN2zYIHfv3pUNGzaIoijSr18/Efnf72XGjBmSK1cu+fLLL8XLy0vKlCmjTruMXga0zwRLfO+mJUuWiJWVlc69gGJiYmT9+vVStmxZKVCggNSqVUtvrRzGujFPyerVq6V169bSrl07nekyf/58tc6Uzm3U946PMdV5+fJlsba2Vg/Janl5eYm1tbUcOnRI/vrrL51+e/bskS1btuh9/ibFYJQOlixZop5Nrz0PI/GC1qVLFylcuLDMmzdPfchlu3btZO/evXprcUnJypUrpWDBgtK/f3+d5x49ePBAXFxcxMfHR6fl6M8//5SePXtm+FVexh46THV+b9++XUaMGCG7du1Su02ZMkUsLS1l0qRJOuHo2bNnkjt3blEURWbPnq23GhMHt7Nnz4qNjY1YW1snO8dk27Zt4uHhIR07dkx2yXtG2rp1qyiKonOT07t374qTk5N07txZZ9i7d+/KlClTpFGjRvL111+rgSOjN5YhISFSp04dyZUrl87DUps2bSqKokiHDh1k9uzZsm3bNrWW169fy40bN9R1gD43SMa0MddKumM2cOBAyZ49uxQrVizZSekLFiyQ6tWrS7NmzfTyoGRTqfPevXsycuRIcXJyUh8d1bJlS3F1dZV27dqpt9aoVq2afPPNN7Jjxw69X32WGgajj3Tw4EFxdXXV2QvTSryS79mzp5QsWVKKFi0q5cqVk2LFiqkz3hCXci5fvlzs7Oxk+fLlOj8S7QZbe5VX7dq15ffff5dbt25J48aNZfLkyeqwGbHgGnvoMNX5vWTJEnFxcZGAgAD1Em2tadOmiaIoMmnSJDVwPnz4UL7//nvZtGmT3jaSKQW3devWSY4cOaRVq1Y6Te8ibx6zkSNHjhRvQJgRYmJiZOLEiZI3b16dq95atmwpiqJIqVKlpGPHjtK4cWPZv3+/PHjwINl76HNaNmnSRKpUqSI3b96U9u3bS6FChWT+/PkyceJE6dSpk1hZWUn16tWlTp06OuuAjF4+jXljLpL6jtmUKVOkUKFCMnDgwGTzdvr06dK9e3e9/rZNoc5Hjx7JmDFjxMHBQYoUKSKenp5qWI+Pj5eHDx/K6NGjpXLlyuLj42M0T3lgMPpI06dPl/r16+us8Pbv3y8jRowQX19fCQgIULuvWbNGJk6cKIGBgXo5DyI1ly9fFg8Pj2Q3x0tISJD79+/rnMjs6ekpuXPnFjc3N53j+hnBFEKHKc7v9evXi729vaxfv15nOiY2adIksbKykp49e8rPP/8sDRs2FF9fX7V/Rm/Q3xbcVq5cKW5ubtK/f/9kV1YdPXpUr9P06dOnMn36dPHw8JCAgABp1aqVlClTRvbs2SMXL16UX3/9VRo3biwlS5YURVFk3rx56rj6PlF4165d0rBhQ8mSJYvky5dPfWSP1pkzZ2TevHnSokULvU1DY9+Yp7RjlvhzR40aJeXKlZPvv/8+2bP3tNOedep69OiR/PDDD+Lo6KhzL6/Xr1/rDKetxxjCEYPRRxo3bpxUrVpVvdngwIEDxdvbW0qWLCkdOnQQW1tbadu2bYrjGqqp8Pjx41K4cGGd8zPWrl0rX331leTIkUPy5s2rPmz12bNncujQIdm1a1eGH/c1hdBhSvM7ISFBnj9/Lg0aNEh2z6nHjx/Lvn37ZNOmTeoKadGiRVKlShXx8PAQPz8/vZ38mJbgtmjRolTDkYh+pq12Ojx79kymTp0qRYoUETs7uxRbhi5fviy//PKLQc6RSDy/du7cKQ0bNpSyZcuqrTRxcXEpbhQzehoa+8b8bTtmiR+IHRgYKOXKlZNhw4aprdZJ68xIplJn4nkVGhoqgYGB4uDgIDNnzlS7J13mDP0oJC0Go4+0bds2KVCggFSpUkXy588vefPmlTlz5qgL4vr168Xa2louXrxoFElY5M3KMnfu3LJ582YJCQmRbt26ScWKFaVly5Yyffp06dmzp1hZWcmRI0eSjZuRK09TCB2mNr9fvnwpZcuWVY/xi4jMmjVLmjVrJoqiiJOTkxQuXFgNJKGhofLs2TO19ox+hMb7BLfFixdLnjx55Kuvvkq2otcXbS1Pnz6VqVOnSvHixdWTrkWS7wWL6OcxJEk3KIl/D/v375cGDRpIpUqV1Pt7GeJO8Ma+MX/XjtnAgQPV6Tx69GjJnTu3TougvhhznYlr0s6vs2fPyqNHj+TZs2cyZswYcXR0THbOoLFhMEoHv/32m/z4448ydOhQefTokc7CsWbNGqlYsaLe7376Ls2aNRMnJyf18tiNGzeqV6ZduXJFXF1dk93zJKOZSugwpfn97Nkz8fT0lJYtW8qqVaukSZMmUqJECenfv78cPHhQTp8+LQULFlSfiZZ4A6uPvbf3DW6zZ8+Wpk2b6m3PMmmASBwYo6KiZOrUqeLh4SF9+/ZVh9HnXm/S8wO1fyIie/fulU2bNonIm8NqjRo1kqpVq+o8Y0xfjHljrvW+O2ZLliwxSKu/sdW5aNEinYf3Jn5Y96ZNmyR37txy6NAhEXlzYcC4ceNEUZRkDyM3JgxGH+FdC9vr16+lcePG0q5dO6NoPRDRrTkoKEh27NiRbEV+5coVKVeunOzdu1ff5Rl16DC1+a2t4dSpU1KsWDHx8PCQypUry+HDh9WnqEdGRkrdunXlu+++M0iNaQ1u3bt3V8fRx2GV4OBgdUchLi5OJ3D8/vvv0qNHD3n9+rV6WK1MmTLSsWPHDKsnJatXrxZFUWTFihVqN+0y+ttvv4mVlZX8+uuvar/du3dLlSpV5Ouvv9ZrnSLGtzFPSVp3zP7++2+d8T7nOu/evas+uqNNmzY6/dauXSu2trYyf/58ne4PHjyQpUuXGuxS/LRgMHpPqTUVJt5zi4yMlFOnTkn9+vXFw8NDHcdQz0VK+rlvO4E6LCxM/P39xdfXV6/1GmvoMKX5nRJtLc+ePUt2xY/Imxur+fj4yLRp0/Rd2kcFt4xcBnbs2CGKokjFihXVc12003HDhg1ia2srixYtUod/9uyZjB49Wv7v//5Pb/M8MjJSbVXLkyePTutKcHCwKIoiCxYsEBHdaaW9T5C+GdPG/G2MeccsMWOp8+XLl9KxY0f1XnL16tVT+40dO1bnfKKUGGs4YjBKg3c1Fbq7u6v3UomKipLOnTtL3bp1pWHDhmoIMcQC8LZm9uDgYJ1DZU+ePJFt27ZJ/fr1pWzZsnq5yZuxhg5Tnd8iqZ/MmPQGjvHx8fLgwQNp2LCheHp6GuxCAGMLbgkJCbJ06VLJnj27eHp6Svny5eX+/fsiInL79m1xdHSUOXPm6AyvrVPfV/tMnTpVChUqJCNHjpR8+fKpe+YPHjxQ7zSslbQmQ4QjY9mYp8RYd8ySMpY6E7/31KlTJU+ePLJ582YpUKCA1K9fP8XhTAmD0Tt8SFPhvn37ZPPmzQa5WZpWWprZf/vtN7XfhAkTpFKlStKhQwe13oy6Rbwxhw5Tnd/vOvTTs2dP9cGNjx8/llGjRkmDBg2kcuXKervxYEqfYYzB7fLly+Lm5ia9e/eWL774QipUqKCGo8T330mJPjZG2uUrMjJSSpYsKd99952MGDFCcuXKpbYSiRhHi6WI8WzMkzLWHTNTrLNRo0by448/yvbt2yVHjhzSoEGDFOs3FQxG7/A+TYUp/agNsXJ6n2b2xP7++2/1OxjL8Wh9hw5TnN9pOfSzePFidfjr16/LF198Id9//32GhuDETCG4JX7/adOmSb169eSXX34RHx8f8fT0VMORoVrXtM+tS2zq1Kny3XffydWrV6V///7i6uoqCxcuVPsbKhwZ68bc2HfMjL3OZcuWSZMmTWT//v3qfahiY2Nl9OjR0r59exF5c6J/jhw5xN/fXx3PWEJ6WjEYpcLUmwrfp5ldX/eSMObQYarz+0MP/SS+X1BGb+iNPbjt379frl69qtMtODhYfH195eLFi3L06FGpXr26VKxYUb1nkb73gteuXas+j23r1q3q/Dt27Jhkz55djh49KmFhYRIQECC5c+fWOQdKX4x1Y65lCjtmxlzn7du3xdbWVhRFkbZt24qnp6csWbJEnj9/LuHh4eLm5qbeNHjXrl3i5uYmlStXTvc69IHBKI2MvanQmJvZTTF0GPv8TsxYD/1o39+Yg5s2tOXIkUPGjx8vy5cvV/t9+eWX0rRpUxF583BLHx8fqVKlit6fh/XixQtp27atKIoiRYoUke7du0uRIkVk27Zt8vz5c5kyZYq0b99e4uPj5caNGzJ48GAxNzeXLVu26K1GY92YJ2bMO2bGXKf2MyIiImThwoWSNWtW+fLLL2X9+vVSvHhxqVu3rgwePFj69u0rPXr0kPj4eImNjZUtW7aIv7+/ybUWiTAYJWOqTYWm1MxuTKHDVOe3iPEf+tEyxuCWkJAgsbGxsmrVKilRooRkzpxZxo0bJ8WKFZNGjRrJ+vXrJTg4WFq2bKnWuHv3bvHw8JCuXbtmSE1vc/LkSenWrZtky5ZNduzYITNnzpTq1atLtWrVpHr16lK2bFm1Ne7atWsyZ84cvc53Y9uYJ2YqO2bGWmdERITEx8dLdHS0iIjMnTtXFEWRhQsXyrNnz2Tr1q1SvXp1MTc3lwIFCqjnCyZe/oxhffk+GIwSMdWmQmNtZjf20GGq89sUDv2ImEZwe/Xqlaxfv16KFCkirVu3lrCwMBk8eLD4+/tL5syZRVEUmTFjhjr8iRMn9Fpv4s86e/astGjRQnLnzi337t2TsLAw+e2336R48eLi7Oyc7CG7ScfPCMa6MX8bY9oxextjqHPTpk3SokULKVeunHz99dfqemf27NmiKIpMnDhRHXb79u1y7do1ETGu+f0hGIzEtJsKjbWZ3ZhDhynPb1M49GPswe3EiROybNkyWbVqlboiX7dunTg7O0vPnj3V4aZOnSqNGjVK8U7RGR04UjuUeP78eWncuLHkypVLfdbho0eP1BPbDb1nbgwbcy1j3zEz9joXLFgg9vb2EhAQIE2aNJFChQqJl5eXukMzd+5cMTc3l1GjRumMZ+qhSITBSERMv6nQGJvZIyMjZfHixeLk5GR0ocMU57epHPox9uC2ZMkScXFxkaJFi4qiKFKlShXZv3+/iLwJR25ubjp3YA4PDxcR/a7sV61aJf7+/jJp0iSJj49P9ls9d+6cNGvWTFxdXeXs2bMi8mZ51GeNxrox1zLmHTNTqHP58uWiKIrs3r1b7TZv3jyxt7eXjRs3isib2yzMmzdPLCwsZPz48Rlekz599sHIlJsKjb2Z/dWrV7Jw4UIxMzMzmtBhyvNbxHgP/ZhCcFu0aJFYWVnJmjVr5PHjx/Lnn39KwYIFpVWrVhITEyMRERGydu1ayZ07t84JxPo8dBYRESF+fn7i7+8vVapUkRo1asiIESPk5s2bOsOdPXtWmjVrJrlz55ZTp07prT4R492Yi5hOa7Ax13nx4kXJlCmTtGjRQudzIiIixN3dXZYtW6Z2i46Olvnz54uiKDrdTd1nHYxMtanQ2JvZEzeZR0dHqy0yhg4dpjq/TeHQj5axBrdff/01xcdkDBo0SPLmzSsvXrzQqT9fvnzi5+eX4XWlZNy4cVKjRg0REVm8eLG0atVKXF1dZcSIETp78NeuXZNq1apJkyZN9FofW4M//Tq/++47qVq1qowePVqePHkiIiIrV64US0tLOX/+vM6w0dHRsnnzZqM6P+tjfbbByFSbCo21mf2PP/6QyZMnS0RERLJ+r1+/NnjoMNX5bQqHfkwhuM2dO1fs7e1lwoQJ6oNMRUSGDh0qZcqUkcePH6vT7NWrV7Js2TJp3ry5QW5rERMTI15eXrJixQr1/j4rVqwQRVEkU6ZM0qZNG/n9998lKipKQkNDDXIYn63Bn16dDx8+1NnpDggIkPLly8vMmTNlxYoV4uDgoB4aT62WTyUcfZbByFSbCo21mf2///4TBwcHyZ07txQtWlR++OEHOXDggM4wkZGRBgsdpjq/TeHQj7EHt8SfM3PmTMmVK5cMGzZMYmNjZceOHWJpaSl//PFHsmFfv36t/q/P4KFtZfn+++/V6RYfHy8VK1aURo0ayb59+8TPz09y5Mgh3bp103uNbA3+NOtcvny5+Pr6ysmTJyUyMlLtPmDAAClevLhYWVnJ9OnTRcTwt//Qh88yGImYblOhMTazh4aGSvPmzeWPP/6QP//8U7p37y6ZMmWSgQMHyq+//qozrHZFqu/QYWrz2xQO/Rh7cEtISFAPVWhNnTpV3N3dpWXLluLg4KAuh4Za2adUo4jI1atXxcXFRX755RepWLGi1KxZU0JCQkTkzTz/66+/9FYzW4M/7TpXrlwpdnZ2Mn/+fHXHJbGhQ4dK0aJFZfz48fLs2TMRMfzVjxntswpGptxUaOzN7LNmzRJ3d3f1eVeXLl2Sli1bio2NjdSrV0/++OMPdcX+22+/6W06Jp6PpjS/jf3Qj7EHt/Xr10ubNm2kUqVKMmTIENm3b5/ab8aMGWJvby8NGjRQr9Y0hKQ1Jm1lHTJkiCiKIg0bNlR/O0nnb0aHI7YGf9p13r9/Xzw9PWXu3Lki8uac1P3790tQUJBcuHBBHa5fv37i6ekp48aNU3csP2WfTTD6FJoKjamZ/eDBgzqH6aKiouSLL77QeexIkSJFpFmzZtKkSROpWLGi2Nvbq89KEsnY0HH//n25deuWhIaG6nQ39vltKod+jDm4rV69WmxsbKRfv37y/fffS8GCBaV69eoyYcIEdRjttB0xYkSKd403VI2TJk1Sh9m6davY29urhyYNsZfO1uBPu847d+5ImTJlJCwsTC5duiTFixeX8uXLS7Zs2aRUqVJqYBIRGThwoLi7u8vSpUsztCZj8FkEI1NtKjTWZnZtk/CPP/4oIv8LFn379pWGDRuKiEjZsmWlWrVqagg9fPiwTJgwQS8rpNWrV0u5cuUkX758kjVrVlmxYoVO/+HDh5vM/DbGQz9axhbcEhIS5MWLF1K3bl2ZNm2a2v3WrVvSu3dvKV++vIwdO1btPn36dMmTJ4/07dtXvXIzo6WlxnHjxqndW7RoIX5+fjrTT9+MsTXYlFr/jbnV+tq1a5IzZ07Zu3ev+Pv7S//+/eX+/fty4sQJ+f7778XNzU1+//13dXh9P2rGUD75YGSqTYXG2sw+f/58sbS0lGrVqkm+fPnUYCHy5sTaQoUKibm5udSoUUMeP36c4ntk5A999erVkilTJlm8eLEcOnRIhg8fLjY2Nsnu4xQQEGDU89sYD/2YQnCLi4uTUqVKyciRI0XkfxubBw8eSN++fcXLy0vWr1+vDj9+/Hhp2rSpXk/CfZ8a169fLzlz5pTDhw/rrT5jbw02ldZ/U2i1fv36tTRq1Ej69u0rdevWlb///lvtd/fuXWnUqJEMGzZM74dwDe2TD0am2FRorM3sCxYsEHNzc/n999/l9u3bUqhQIZk3b56IvDn3KTY2VgYOHCilSpVSw5o+/fPPP1KpUiWdFbiIiKenp0ydOlWtU2vQoEFGPb+N6dCPKQS3+Ph4iYyMFH9/f+nYsaPExsZKQkKC+tu4ffu21KhRQ+cqOZH/BRN9hKO01qg9WT08PFw6deqktw2RsbcGm0rrvym1Wh89elQURRFFUZIF8A4dOkiHDh0MUpchffLByJSaCo25mX3RokWiKIps3rxZRN6sMP38/KRmzZo6wx0/flwsLS3VZ7Hpc0/8zp07UqlSJbl8+bLOZ9evX18CAgLU4RKvgH766Sejnt+GPvQjYvzBLSoqSuf1zp07xczMTObMmaN2087zbdu2iZWVldy8eVNnvmf0cvohNSZ93lxGL6fG3hpsKq3/pthqffDgQVEURVq0aCEXL14UkTcn1fv5+cmYMWMMWpshfPLByNSaCo21mf348eNq2NGu/I4fPy5OTk6yatUqnVp79eolXl5eBmk1unfvnvq/9rDPV199pU5PraTN26Ywv0X0e+jHFILbxo0bZcSIEcmWtR9//FG9+WBiQUFBUq5cuVQ37J9rjcbeGixiGq3/ptpqLfImHOXLl0+KFSsmTZo0kapVq0qpUqWM4jY1+vbJByMR02kqNPZm9qQePXokPj4+6rOutHXOmjVL7+dtJJWQkKB+focOHaRXr15q99atW8uiRYsMVpuWKRz6MebgtnnzZvV3/f333+sEiZcvX8rYsWNFURQJCAiQHTt2yOXLl6VevXpSu3ZtvS2bplCjKbQGi5hG67+ptVondfPmTZk+fbr06NFDJk6cqIYiY6lPXz6LYCRi3E2FptDMnpqVK1eKmZmZnD59Wqe7tl5juNqrXbt26qMpGjZsKLly5dLZa9M3Uzj0o63BWIPb/fv3pWnTpjJ27FhZunSpKIoigwYNStYSuG7dOilcuLDkzJlTihcvLl5eXuq8z+hl0xRqFDGd1mBTaf03tVbrdzHWujLSZxOMRIyzqdAUmtnf5unTp1KtWjXp27evxMXF6X3j/TbaFWSPHj1k8ODB0rp1aylcuLC60THEfDeF+W0Kwe3ly5cyf/589WrNdevWpRo8Hj58KJcvX5YzZ86odetj3ptCjakx1tZgU2n9FzGNVmtK2WcVjESMq6nQFJrZ02LIkCGSOXNm9W7HxqZr166iKIqUL1/eoKHIFOa3KQQ3raQBbu3ataIoigwcOFA9mfX58+dy6dIlneH02YppCjWmxlhbg4259T81xtZqTW/32QWjlBgiFJlKM/vbaDfWt27dki+++MJom1wPHTokhQsXVsOQIUKRKcxvUwhuKYmPj1c/Xxs8Bg8eLJcuXRJfX1/55ptvDFablinUmJQxtwYbY+t/Soyx1ZrejcHIQEy5mT2pxBtsYw1H2hW5oaabsc9vUwhub5P43Kf169eLhYWFODo66myEDM0UakzKmFuDjan1/12MpdWa0obByIBMuZndFBl6L9eY57exB7e0SDx/CxQoINWrVzdoK2FKTKFGEdNpDU7KWOs0hlZrSjsGIyNgis3s9OGMdX4bc3BLq8jISKlTp464ubkZ7UbIFGrUMoXWYFNh6FZrSjtFRARkcPImpMLMzAwbNmxA+/btYW9vj5w5c+LSpUuwtLQ0dImUjox5fickJEBRFCiKgnXr1qFdu3YYNGgQOnXqhL59+6Jw4cKYN2+ewep7m9jYWGzevBnNmzeHpaUl4uLiYGFhYeiydJhCjZQxRASKohi6DHoHBiMjkvhHU7BgQbi5uSE4OBgWFhZceX6CjHl+G3NwSytDT8O0MIUaiT43DEZG5tWrV2jatCn++ecf/Pfff0axkaSMY8zz25iDGxFRRjEzdAGky9LSEt26dcPt27e5AfoMGPP8VhQFr169Qt26dfH69WuGIiL6LLDFyIhxA/R5Mcb5zfNhiOhzw2BERGnCUEREnwMGIyIiIiINnmNEREREpMFgRERERKTBYERERESkwWBEREREpMFgRERERKTBYERERESkwWBERGkSGBiIsmXLGroMk9a5c2c0a9bM0GUQ0VswGBERFEV561/nzp0xcOBA7N271yD1JSQkYMiQIXBzc4OtrS1Kly6NLVu2vHO8KlWqoGfPnjrd5s2bB0VRsGTJEp3uXbt2hZeXV7rUe/v2bSiKgnPnzqXL+xGR/vA2tkSEhw8fqv+vX78eo0aNwpUrV9Rutra2yJQpEzJlymSI8rB69WrMmDEDK1euRJUqVXD9+vU0jVerVi1s3rxZp9v+/fvh7u6O4OBgdO3aVad727Zt07VufYiPj4eiKDAz434uUXrgL4mI4OLiov45OjpCUZRk3ZIeStMeFpowYQKcnZ2RJUsWjBkzBnFxcRg0aBCcnJyQO3duLF26VOez7t+/jzZt2iBr1qzIli0bmjZtitu3b7+1PjMzM+TIkQNt27ZFvnz5UKdOHdSpU+ed36tWrVq4cuWKTvA7cOAAhg4div3796vd7t69i5s3b6JWrVoAgH/++QcNGzZEpkyZ4OzsjA4dOuDJkyfq8Dt37kT16tWRJUsWZMuWDf7+/rhx44baP3/+/ACAcuXKQVEU+Pj46NQ1depUuLq6Ilu2bPj2228RGxur9ouJicHgwYORK1cu2Nvbo3Llyjq1Ll++HFmyZMHWrVtRokQJWFtb47///nvntCCitGEwIqIPtm/fPjx48AAHDx7E9OnTERgYCH9/f2TNmhXHjx/HN998g2+++QZ3794FALx69Qq1atVCpkyZcPDgQRw+fBiZMmVC/fr1ERMTk+rn+Pr6IiwsDCNHjnyv+qpVqwZLS0s1WPzzzz+IiorCV199hfDwcFy7dg0AEBwcDCsrK3h5eeHhw4fw9vZG2bJlcerUKezcuROPHj1C69at1feNjIzEgAEDcPLkSezduxdmZmZo3rw5EhISAAAnTpwAAOzZswcPHz7Eb7/9po4bHByMGzduIDg4GCtWrMDy5cuxfPlytX+XLl3w119/Yd26dTh//jxatWqF+vXrq7Vqp+PEiROxePFiXLp0CTlz5nyv6UJEbyFERIksW7ZMHB0dk3UfPXq0lClTRn3dqVMnyZs3r8THx6vdihYtKjVq1FBfx8XFib29vaxdu1ZERJYsWSJFixaVhIQEdZjo6GixtbWVXbt2pVhPZGSklCxZUrp16yaVK1eWAQMG6Izv4OAgv/76a6rfx8vLS7p37y4iIj///LM0bNhQRETq168vCxcuFBGRLl26qHWPHDlS/Pz8dN7j7t27AkCuXLmS4meEhoYKALlw4YKIiNy6dUsAyNmzZ3WG006zuLg4tVurVq2kTZs2IiJy/fp1URRF7t+/rzOer6+vDB06VETezB8Acu7cuVS/MxF9OLYYEdEHK1mypM65Lc7OzihVqpT62tzcHNmyZUNoaCgA4PTp07h+/TocHBzUc5acnJzw+vVrnUNRiS1fvhwvXrzAnDlzsGPHDuzZswedO3dGXFwcbt++jZcvX771pOlatWqpLUb79+9XD2t5e3vrdK9du7ZaY3BwsFpfpkyZUKxYMQBQa7xx4wbatWuHAgUKIHPmzOqhszt37qRpmpmbm6uvXV1d1elz5swZiAiKFCmi8/kHDhzQmT5WVlYoXbr0Oz+LiN4fT74mog9maWmp81pRlBS7aQ8xJSQkoEKFCvjll1+SvVeOHDlS/Izz58+jZMmSsLKygpWVFYKCglCjRg00b94chQsXRv369eHq6ppqjbVq1cIPP/yA+/fv48CBAxg4cCCAN8Fo9uzZuHPnDm7duqWeX5SQkIDGjRtj0qRJyd5L+zmNGzeGu7s7Fi1aBDc3NyQkJMDDw+OthwO13jV9zM3Ncfr0aZ3wBEDnxHdbW1soivLOzyKi98dgRER6U758eaxfvx45c+ZE5syZ0zROrly5sHnzZkRERMDBwQE5c+bEnj17UKNGDWzduhWnT59+6/heXl6wtrbG3LlzERUVhQoVKgAAPD09ERYWhgULFsDGxgZVqlRRa9y0aRPy5csHC4vkq8inT5/i8uXLWLBgAWrUqAEAOHz4sM4wVlZWAN5cMfY+ypUrh/j4eISGhqrvTUT6xUNpRKQ37du3R/bs2dG0aVMcOnQIt27dwoEDB/Ddd9/h3r17KY7TtWtXxMfHo0mTJjhy5AiuXLmCP/74Ay9evICdnR0WL1781s+0tbVF5cqVMXv2bFSrVk1tibG0tETVqlUxe/ZsNTwBwLfffotnz57hyy+/xIkTJ3Dz5k3s3r0bX331FeLj49Wr6RYuXIjr169j3759GDBggM5n5syZE7a2tuqJ22FhYWmaPkWKFEH79u3RsWNH/Pbbb7h16xZOnjyJSZMmYfv27Wl6DyL6OAxGRKQ3dnZ2OHjwIPLkyYMWLVqgePHi+OqrrxAVFZVqC5KbmxtOnDiB7Nmzo0WLFihXrhzWrVuHNWvWYNu2bVi0aBGmT5/+1s+tVasWIiIikl027+3tjYiICPUwmvbz/vrrL8THx6NevXrw8PDAd999B0dHR5iZmcHMzAzr1q3D6dOn4eHhgf79+2PKlCk672thYYGffvoJCxYsgJubG5o2bZrmabRs2TJ07NgRAQEBKFq0KJo0aYLjx4/D3d09ze9BRB9OERExdBFERERExoAtRkREREQaDEZEREREGgxGRERERBoMRkREREQaDEZEREREGgxGRERERBoMRkREREQaDEZEREREGgxGRERERBoMRkREREQaDEZEREREGv8PgSP1Aux5Hh8AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Preparing seaborn barplot\n",
    "\n",
    "sns.barplot(x='concatenated',y='Counts',hue='Y', data=sorted_filtered_df)\n",
    "\n",
    "# Add labels and title\n",
    "plt.xlabel('Time & Weather')\n",
    "plt.ylabel('Counts')\n",
    "plt.title('Coupons by The Time of Day & Weather Conditions')\n",
    "plt.xticks(rotation=45)\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As anticipated, the data indicates higher acceptance rates for coupons when the weather is sunny. However, for coffee house coupons, the time of day remains a critical decision factor. Overall, there is an increased number of accepted coupons on sunny days, with the proportion of accepted versus rejected coupons significantly favoring acceptance at 10 a.m. and 2 p.m. Additionally, the time of day is also a crucial factor in coupon acceptance on both snowy and rainy days."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4.1 What is the relationship between direction, coupon duration, & acceptance rate? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>direction</th>\n",
       "      <th>expiration</th>\n",
       "      <th>Y</th>\n",
       "      <th>Counts</th>\n",
       "      <th>concatenated</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Same_Dir_No</td>\n",
       "      <td>1d</td>\n",
       "      <td>0</td>\n",
       "      <td>570</td>\n",
       "      <td>Same_Dir_No_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Same_Dir_No</td>\n",
       "      <td>1d</td>\n",
       "      <td>1</td>\n",
       "      <td>782</td>\n",
       "      <td>Same_Dir_No_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Same_Dir_No</td>\n",
       "      <td>2h</td>\n",
       "      <td>0</td>\n",
       "      <td>1079</td>\n",
       "      <td>Same_Dir_No_2h</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Same_Dir_No</td>\n",
       "      <td>2h</td>\n",
       "      <td>1</td>\n",
       "      <td>815</td>\n",
       "      <td>Same_Dir_No_2h</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Same_Dir_Yes</td>\n",
       "      <td>1d</td>\n",
       "      <td>0</td>\n",
       "      <td>166</td>\n",
       "      <td>Same_Dir_Yes_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Same_Dir_Yes</td>\n",
       "      <td>1d</td>\n",
       "      <td>1</td>\n",
       "      <td>251</td>\n",
       "      <td>Same_Dir_Yes_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Same_Dir_Yes</td>\n",
       "      <td>2h</td>\n",
       "      <td>0</td>\n",
       "      <td>186</td>\n",
       "      <td>Same_Dir_Yes_2h</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Same_Dir_Yes</td>\n",
       "      <td>2h</td>\n",
       "      <td>1</td>\n",
       "      <td>147</td>\n",
       "      <td>Same_Dir_Yes_2h</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      direction expiration  Y  Counts     concatenated\n",
       "0   Same_Dir_No         1d  0     570   Same_Dir_No_1d\n",
       "1   Same_Dir_No         1d  1     782   Same_Dir_No_1d\n",
       "2   Same_Dir_No         2h  0    1079   Same_Dir_No_2h\n",
       "3   Same_Dir_No         2h  1     815   Same_Dir_No_2h\n",
       "4  Same_Dir_Yes         1d  0     166  Same_Dir_Yes_1d\n",
       "5  Same_Dir_Yes         1d  1     251  Same_Dir_Yes_1d\n",
       "6  Same_Dir_Yes         2h  0     186  Same_Dir_Yes_2h\n",
       "7  Same_Dir_Yes         2h  1     147  Same_Dir_Yes_2h"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts3 = coffee_house.groupby(['direction_same','expiration','Y']).size().reset_index(name='Counts')\n",
    "\n",
    "# Replace 'value2' with 'new_value' in 'Column1'\n",
    "counts3['direction_same'] = counts3['direction_same'].replace(0, 'Same_Dir_No')\n",
    "counts3['direction_same'] = counts3['direction_same'].replace(1, 'Same_Dir_Yes')\n",
    "\n",
    "# Concatinate two string columns for clear charting\n",
    "counts3['concatenated'] = counts3['direction_same'].str.cat(counts3['expiration'], sep='_')\n",
    "\n",
    "# Rename direction column\n",
    "counts3.rename(columns={'direction_same': 'direction'}, inplace=True)\n",
    "\n",
    "counts3.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>direction</th>\n",
       "      <th>expiration</th>\n",
       "      <th>Y</th>\n",
       "      <th>Counts</th>\n",
       "      <th>concatenated</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Opp_Dir_No</td>\n",
       "      <td>1d</td>\n",
       "      <td>0</td>\n",
       "      <td>166</td>\n",
       "      <td>Opp_Dir_No_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Opp_Dir_No</td>\n",
       "      <td>1d</td>\n",
       "      <td>1</td>\n",
       "      <td>251</td>\n",
       "      <td>Opp_Dir_No_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Opp_Dir_No</td>\n",
       "      <td>2h</td>\n",
       "      <td>0</td>\n",
       "      <td>186</td>\n",
       "      <td>Opp_Dir_No_2h</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Opp_Dir_No</td>\n",
       "      <td>2h</td>\n",
       "      <td>1</td>\n",
       "      <td>147</td>\n",
       "      <td>Opp_Dir_No_2h</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Opp_Dir_Yes</td>\n",
       "      <td>1d</td>\n",
       "      <td>0</td>\n",
       "      <td>570</td>\n",
       "      <td>Opp_Dir_Yes_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Opp_Dir_Yes</td>\n",
       "      <td>1d</td>\n",
       "      <td>1</td>\n",
       "      <td>782</td>\n",
       "      <td>Opp_Dir_Yes_1d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Opp_Dir_Yes</td>\n",
       "      <td>2h</td>\n",
       "      <td>0</td>\n",
       "      <td>1079</td>\n",
       "      <td>Opp_Dir_Yes_2h</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Opp_Dir_Yes</td>\n",
       "      <td>2h</td>\n",
       "      <td>1</td>\n",
       "      <td>815</td>\n",
       "      <td>Opp_Dir_Yes_2h</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     direction expiration  Y  Counts    concatenated\n",
       "0   Opp_Dir_No         1d  0     166   Opp_Dir_No_1d\n",
       "1   Opp_Dir_No         1d  1     251   Opp_Dir_No_1d\n",
       "2   Opp_Dir_No         2h  0     186   Opp_Dir_No_2h\n",
       "3   Opp_Dir_No         2h  1     147   Opp_Dir_No_2h\n",
       "4  Opp_Dir_Yes         1d  0     570  Opp_Dir_Yes_1d\n",
       "5  Opp_Dir_Yes         1d  1     782  Opp_Dir_Yes_1d\n",
       "6  Opp_Dir_Yes         2h  0    1079  Opp_Dir_Yes_2h\n",
       "7  Opp_Dir_Yes         2h  1     815  Opp_Dir_Yes_2h"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts4 = coffee_house.groupby(['direction_opp','expiration','Y']).size().reset_index(name='Counts')\n",
    "\n",
    "# Replace 'value2' with 'new_value' in 'Column1'\n",
    "counts4['direction_opp'] = counts4['direction_opp'].replace(0, 'Opp_Dir_No')\n",
    "counts4['direction_opp'] = counts4['direction_opp'].replace(1, 'Opp_Dir_Yes')\n",
    "\n",
    "# Concatinate two string columns for clear charting\n",
    "counts4['concatenated'] = counts4['direction_opp'].str.cat(counts4['expiration'], sep='_')\n",
    "\n",
    "# Rename direction column\n",
    "counts4.rename(columns={'direction_opp': 'direction'}, inplace=True)\n",
    "\n",
    "\n",
    "counts4.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       direction expiration  Y  Counts     concatenated\n",
      "0    Same_Dir_No         1d  0     570   Same_Dir_No_1d\n",
      "1    Same_Dir_No         1d  1     782   Same_Dir_No_1d\n",
      "2    Same_Dir_No         2h  0    1079   Same_Dir_No_2h\n",
      "3    Same_Dir_No         2h  1     815   Same_Dir_No_2h\n",
      "4   Same_Dir_Yes         1d  0     166  Same_Dir_Yes_1d\n",
      "5   Same_Dir_Yes         1d  1     251  Same_Dir_Yes_1d\n",
      "6   Same_Dir_Yes         2h  0     186  Same_Dir_Yes_2h\n",
      "7   Same_Dir_Yes         2h  1     147  Same_Dir_Yes_2h\n",
      "8     Opp_Dir_No         1d  0     166    Opp_Dir_No_1d\n",
      "9     Opp_Dir_No         1d  1     251    Opp_Dir_No_1d\n",
      "10    Opp_Dir_No         2h  0     186    Opp_Dir_No_2h\n",
      "11    Opp_Dir_No         2h  1     147    Opp_Dir_No_2h\n",
      "12   Opp_Dir_Yes         1d  0     570   Opp_Dir_Yes_1d\n",
      "13   Opp_Dir_Yes         1d  1     782   Opp_Dir_Yes_1d\n",
      "14   Opp_Dir_Yes         2h  0    1079   Opp_Dir_Yes_2h\n",
      "15   Opp_Dir_Yes         2h  1     815   Opp_Dir_Yes_2h\n"
     ]
    }
   ],
   "source": [
    "# Union the DataFrames\n",
    "df_union = pd.concat([counts3, counts4], ignore_index=True)\n",
    "\n",
    "print(df_union)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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MUO33XbbNZ0KejV58+ZVvnz5NHfuXI+rK9auXVtff/21li5dqlmzZmns2LHy87vysWK20Tfmo48+0owZM/Thhx9q4cKFOn369GXfa5duW9atW6cDBw4k2bZcK5fLJT8/P4+DKOfPn9cnn3ySpG16ew0DyWFkC0iBatWqady4cerevbsqV66sp59+WmXLllVMTIy2bdumiRMnqly5cnrooYdUunRpde3aVaNHj5aPj48aN26s/fv365VXXlFYWJjHjlf79u31+OOPq3v37mrZsqUOHDigYcOGXfZ7S8eOHdN//vMfdenSRWfOnNFrr72moKAgDRgwQNLFkYphw4bpscceU9OmTdWtWzdFRUXp3Xff1enTp/X222+nyvpIGNXq16+f7rnnniTzz549q+XLl2vGjBl69tlnNWbMGD300EO699579dxzz6lQoUI6ePCglixZ4v7gHj58uO6//35VrVpV/fv3V4kSJfTXX39p4cKFmjBhgrJly6bXX39dS5cuVfXq1dWrVy+VLl1aFy5c0P79+/XNN99o/PjxHkeqfX19Vb9+ffXp00fx8fF65513FBER4b7cuCR3eBk1apQ6dOggf39/lS5dWtWrV1fOnDn11FNP6bXXXpO/v78+/fRT7dixI8XrrW3btpo6daqeeuop7dmzR7Vr11Z8fLw2btyoMmXKqE2bNrrvvvvUtWtXPfnkk9qyZYseeOABZcmSRUePHtXatWtVvnx5Pf3001d9rHnz5snPz0/169fXrl279Morr+jOO+9U69atPdrlyJFDTzzxhMaNG6fChQsn+Z7TlcTHx2vDhg2SLl7S/uDBg1q8eLE+//xzlSlTRp9//vn1raBk/Pe//1W3bt105MgRVa9ePVVG3RJ06NBBI0aM0OOPP64333xTJUqU0OLFi7VkyRJJuuLpnon9+uuv2rBhg+Lj490/ajx58mRFRETo448/TvFl9Hv37q25c+fqgQce0HPPPacKFSooPj5eBw8e1Hfffae+ffuqatWqqlGjhtq3b68333xTf/31l5o2barAwEBt27ZNmTNnVs+ePSVdfK3PmjVLs2fPVrFixRQUFHTZ8D506FDVr19ftWvX1vPPP6+AgACNHTtWO3fu1GeffXZdI5SX4+vrq1GjRqldu3aqVq2annvuORUpUkQHDhzQlClTFBQUpCxZsuill17Sd999d8XRaLbRyUv8Hr1UpUqVFBgYqJ9//lm9evVShw4d3AFr8uTJatWqlUaOHJnkzIUtW7aoc+fOeuSRR3To0CENHDhQBQsWVPfu3VPUxyZNmmj48OFq166dunbtqpMnT+q9995LdhQ/vb2GgWR55bIcQAaxfft269ChgxUqVMgCAgLcl9N+9dVXPa6iFxcXZ++8846VKlXK/P39LU+ePPb444/boUOHPO4vPj7ehg0bZsWKFbOgoCCrUqWKrVix4rJXuvrkk0+sV69eljdvXgsMDLQaNWrYli1bkvRzwYIFVrVqVQsKCrIsWbJY3bp17YcffvBoc7kfv03uammJRUdHW758+ZJcxS6x2NhYu+2226x8+fLuaevXr7fGjRtbcHCwBQYGWvHixZNcMe9///ufPfLII5Y7d24LCAiwQoUKWceOHT1+pPT48ePWq1cvK1q0qPn7+1uuXLmscuXKNnDgQIuMjDSzf69M9c4779jgwYPttttus4CAAKtUqZItWbIkSX8HDBhgBQoUMB8fH48r261bt86qVatmmTNntrx581rnzp3txx9/THLVq8tdmS9hHSd2/vx5e/XVV61kyZIWEBBguXPntjp16rgvR59gypQpVrVqVcuSJYtlypTJihcvbk888USy9U7uMbdu3WoPPfSQZc2a1bJly2Zt27a1v/76K9llVq1aZZLs7bffvuJ9J3bplc4yZcpkhQoVsoceesimTJliUVFRSZYpXLiwNWnSJNn7u9xV386cOWOZMmW67FUcL3c1wmutx8GDB61Fixbu9dSyZUv75ptvTNJVfwQ34bET/vz8/Cx37txWrVo1e+mll2z//v1Jlrnc1QjLli2b7GNERkbayy+/bKVLl7aAgAALDg628uXL23PPPefxMwBxcXE2YsQIK1eunLtdtWrV7KuvvnK32b9/vzVo0MCyZcvm/nkAs+Sv5GZmtmbNGqtTp477NXjvvfd63F/i53PpFROTq8vlrF692ho3bmw5cuQwf39/9yW4Dx48aGvXrrWgoCCrUaOG+/19JWyj/3WlqxFKsl9//dUiIyPt9ttvtzvuuCPJZfefeeYZ8/f3t40bN3o87nfffWft27e3HDlyWKZMmezBBx+0X3/9NcljJ3c1wmeeeSbZvk6ZMsVKly5tgYGBVqxYMRs6dKhNnjw5yfNMr69hIDGX2TVeGglAurFq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vNHVW8qGDRusQIECtnfvXjO7uP7NzFauXGkBAQHWqVMn+9///ufNLmYo8fHxFh8f7975XL9+vQUFBZnL5bKhQ4e625hdDFxFihSxpk2b2oYNG7zW54xm9+7dFhoa6t7uREVFmZnZgQMHLHfu3NaoUSNbs2YNB9tSScJ6TAhPJ0+etKJFi5rL5bJnn33Wo21C4KpUqZJ99dVXhF6HxMfH27lz56xGjRr26quveswbOnSo5c2bl8DlgMTblLfeesvuvfde69ixo7Vp08bj4MKkSZOsWrVq1qFDB/vll19S7fE5jRCOu/S0hGzZsmn79u06ffq0pIvD6qGhoXrkkUd0/vx51a5dW+vXr/dCTzOmxBfCyJs3r4YNG6annnpK+/bt05EjRyRd/D6Fn5+f3njjDfXr109t27bVsmXLvNXlW0K+fPl08uRJ92s94TSr0qVLq2DBgpoyZYqmT5/uzS5mKDExMYqOjnav53vvvVfr169XlixZtGLFCu3bt899GnPJkiW1dOlSLV26VHPmzPFyzzOOwoULy+Vyae7cuZKkgIAAxcXFKTg4WMWKFdOSJUs0adIkj20WUu7s2bOKiIhwfzclV65c2rZtm8qUKaMlS5Zo27Zt7lM3/f39tXLlSp07d05z5szh+7upLGE9u1wuBQUFKSgoSJGRkZL+vUBV//79VatWLc2ePVuvvvqq/vzzT6/1N6NJvE156aWX1LhxY3333XfasmWLx/e0OnfurE6dOun3339Xv379dPDgwdTpQKrFNuASO3fudP+f+MjBTz/9ZPfcc4/16dPHwsPD3dN/+OEH69Spk3344Yfuo/y4MatWrbJ33nnHXn31Vfvyyy/d048ePWodO3a0zJkz29q1a83s3yM/0dHRNn78eGqQSpYuXWpbtmzxmJZw1PjFF1+0woULe5xWdebMGevVq5dt3LiR03lSybx586xly5ZWpUoVa9u2rUVERLjnbdq0yYKCgqxdu3Z28OBBM/v3vXDo0CFqkAJffvmlLViwwGNawnocN26cFSpUyN5//333vKioKOvSpYv98ssvrO9UMnv2bKtXr56VKVPG7rnnHo/Tkk+dOmVFihSxe++913bs2OGxXExMDDVIRSdPnnT/n3h05ZlnnrHChQvbX3/9ZWb/fia88MILVqFCBevevTuji6lkz549tnHjRvvxxx8tMjLSPf29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NmjQIAsODrZ9+/Z53MeECRMIvDcgI9SAsIVknT592tq1a2dlypSxzz77zD39tddes7CwMNu6datH+08++cTuu+8+jyNuX375pQUFBdmcOXPSrN8ZCTXwrvj4eI+d9SlTptjTTz9tTz31lE2bNs3MLp7G8/vvv3ssV7NmTXvuuefct3/++WfLlSuXzZo1K206noFQA+/Ytm2blS9f3kqVKmWnT582s4unadauXdvatWvnHkExMzt27JjdeeedHgHgjz/+sFKlSnlst3B9qIH3Jd72HDhwwA4ePGhnzpwxs4vfgWvcuLFNnDjRvWN/6NAhu/vuu23nzp3u5d5//31OW74BGaUGhC1c1o8//midOnWyypUru78XYWZWrVo1K1WqlK1atcqOHDliERERVqdOHfvPf/7jsfzChQvd55YjZaiB9yQOrS+88IIVKFDAevbsaf379zeXy2XPP/+8e35kZKStWbPGGjZsaBUqVPAYXYyIiLBff/01TfueUVAD79mxY4fdc889VrRoUffoyuLFi61s2bLWtGlTe+edd+ybb76xevXqWaVKlTx2ii5cuGB//vmnl3qecVAD70k8ijJ48GCrWLGi3X777Va0aFH3wcuE9R0XF2fnz5+3Ro0aWe3atT1G4tu3b+/x2Y1rl5FqQNjCFW3dutU6duxolStXdh9Jjo2NtVq1alnhwoWtQIECVqlSJatQoYL7vPKrXRUM14capL1vvvnGGjZsaHFxcbZs2TIrWrSo+8p18+bNs8DAQBs/frxH+8cee8wefPBBdw242tSNoQZp6++///a4HRcXZ9u3b7cqVapYkSJF3POXLVtmnTp1spCQEKtcubI1atTIvb4T7+zj+lGD9GHdunXuHf3Bgwdb3rx5bdGiRe6L8oSGhroP3pw/f94mTZpkNWvWtLvuuottTyrJaDUgbMHt66+/ttmzZ3ucnmB28XSGJ554wipVquTe2Tcz++qrr2zatGn26aefujfw6enFfTOiBunD4MGDrWzZsmZmNnPmTHvggQfM7OJOftasWW3ChAlmZnbmzBlbv369xcfH244dO9whlxrcOGqQdmbPnm0VK1a0xx57zL777jvbsWOHe94vv/xi99xzj4WFhbl39s+fP2+nT5+28PBw9w4R6/vGUIP04cCBA5Y5c2ZbvXq1RUZGWp06dWz27NlmdvG0/Bw5ctjY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6X3UIG0RttJQ4hd3nz59LGfOnJYjRw4LCAiwMWPGeLTdsmWLtWnTxsqUKWPLly9P665mWNTA+xhV9D5qkLbCw8Pt4MGDtmPHDouIiLBz587Zgw8+aC6Xy95//32LjY11t42IiLC8efPaBx98YGb/brPmzJljuXLlcp/ehutDDdIHTuH0PmqQ9ghbaSTxi/u3336z8uXL24YNG+ybb76xjh07WvHixW3KlCkey6xfv95eeeUVjw8BpBw18D5GFb2PGqStmTNnWo0aNSx//vzmcrksLCzMBg0aZGfOnLH69etbxYoVbd68ee72p0+ftrJly9rkyZPN7GK9Emp29uxZrzyHmx01SH84hdP7qEHaIWylsffee8/atm1rzz77rHva7t27rUePHla6dOkkO/sJ2NlPPdTAOxhV9D5qkLamTJliQUFBNmbMGFu+fLl9//331rFjR/P19bUOHTpYeHi41atXz4oVK2bdunWzMWPGWPPmza106dLJjhwScq8fNfA+TuH0PmrgXYStNHT27Fnr27evZc2a1Ro3buwxL2Fn/4477vC4xDJSFzXwDkYVvY8apK1t27ZZ8eLFbfbs2R7TT5w4YWPGjDF/f3977rnnLCYmxho2bGgul8tatWplgwcPdrdlvd8YapA+cAqn91ED7yJsOSjhBZp4J2f//v322muvmcvlcv9AaIJffvnFHn/8cWvbti1Hz1IJNUhfGFX0PmqQNhYuXGgVK1a0o0ePutddwjbl1KlTNnDgQMucObPt3LnTTp06ZQ888IA1atTIvv76a/d9sA26MdTA+ziF0/uogfcRthyS+HsRkZGRduHCBfftQ4cO2UsvvWRZs2a18ePHeyy3f/9+97Js5G8MNUhfGFX0PmqQdgYNGmQhISHu25duS/bs2WN+fn7ucHvixAm77777rEaNGjZv3jy2PamAGngXp3B6HzVIHwhbDki8kz9ixAhr2LCh1atXz55++mn39EOHDtnAgQMte/bsNnHixCveB64fNfA+RhW9jxp4z+zZsy1z5sweXz5PLCYmxm677TYbN26ce9rJkyetbNmy1qhRI4uMjEyrrmZY1MB7OIXT+6hB+kHYclD//v0tNDTU3n77bRs7dqzlyZPH45e3Dx06ZK+88oq5XC73b9ogdVED72BU0fuogXf9/vvvFhwcbC1btrSDBw+6pyfsvPz+++9WsWJF98VHErZJf//9t+3bty/N+5sRUQPv4RRO76MG6QdhKxUl3plZsGCB3XHHHfbDDz+Y2cUruWTJksUyZ85s999/v3ujvn//fpswYQK/WZNKqIH3MarofdQgfZg5c6YFBgbaY489Zj/++KN7+rlz56xJkyb2wAMPeKxnjiKnPmrgHZzC6X3UIP0gbKWSJUuW2LvvvmubN282s4tXbRkyZIiZmX399deWK1cuGzNmjK1YscL8/f3t4YcfTvKjcOzs3xhqkL4wquh91MC7YmJibNKkSebv728FCxa0Bx980Nq1a2c1atSwO++80739YQffOdTAOziF0/uoQfpB2EoFU6ZMsYIFC9rTTz9tmzZtck/fv3+/RUREWPXq1e2NN94wM7MjR45Y6dKlzeVyWZcuXbzV5QyHGngfo4reRw3Sp23btln37t2tdu3a1qFDB3v77bfd65v1njaoQdriFE7vowbpB2HrBn322WeWOXNmmz17tp05cybJ/H379lmhQoXcpy8cPXrU2rdvb5s3b+ZIWiqhBt7HqKL3UYObD9sf76MGzuEUTu+jBukDYesG/PXXX/bAAw8kuUzy2bNnbePGjbZp0yY7deqUlStXzpo3b26rV6+2evXqWd26dd0vbl7YN4YaeB+jit5HDdI/vv/gfdQgbXEKp/dRg/TBR7ghx48fV8GCBd23x40bpyeffFL33nuvmjVrpubNm2vw4MHau3evunTpoqioKC1evFg+Pj6Kj4+Xr6+vF3ufMVAD75k1a5Z69Oih4cOH6+2339bdd9/tnle4cGGdPHlShw8fVpMmTSRJLpdL99xzjzZt2qRx48Z5q9sZCjW4ObhcLm934ZZHDdKWn5+fOnfurE2bNql58+Y6f/68/P391aRJE23ZskX+/v6KjY3lM9hB1CB98PN2B252ERER+vrrr5U9e3aNHTtWe/bs0f33368lS5bozJkzevnll7V7925t2LBBf/75p0qXLi0fHx/FxsbKz4/VnxqogXccO3ZM48aN07Bhw9S6dWv39MjISP3vf/+Ty+VSyZIllT17dg0ePFh9+vTRG2+8ITPTXXfdJR8fH8XFxbGRvwHUAEB6V7FiRY0ZMybJ9Li4OD6D0wg18C7W8A3Ily+fpk+frpYtW2rFihXKli2bRo0apQoVKihPnjw6deqU3nzzTUVFRSl79uzKnj27JCk+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\n",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Preparing seaborn barplot\n",
    "plt.figure(figsize=(10, 6))\n",
    "\n",
    "# Preparing seaborn barplot\n",
    "sns.barplot(x='concatenated',y='Counts',hue='Y', data=df_union)\n",
    "\n",
    "# Add labels and title\n",
    "plt.xlabel('Direction & Expiration')\n",
    "plt.ylabel('Counts')\n",
    "plt.title('Coupon Acceptance by Driving Direction & Coupon Expiration')\n",
    "plt.xticks(rotation=45)\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Regardless of direction, coupons that expire in one day are accepted more frequently than those that expire in two hours."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Findings Summary:\n",
    "\n",
    "#### 1.1 How does the coffee house coupon acceptance rate compare to the bar coupon acceptance rate?\n",
    "\n",
    "A total of 49.1% of respondents accepted the coffee house coupon. The acceptance rate for coffee house coupons is slightly higher compared to bar coupons, which had an acceptance rate of 41%.\n",
    "\n",
    "#### 2.1 How do gender and age affect the acceptance of coffee house coupons?\n",
    "\n",
    "Through analysis of the barplot presented earlier, it becomes evident that females aged below 26 exhibit higher acceptance rates compared to males within the same age bracket. Conversely, both females and males aged 50 and above display the lowest coffee house coupon acceptance rates. In the context of analyzing gender, age, and acceptance rate, age emerges as the more pivotal feature, overshadowing gender's influence.\n",
    "\n",
    "#### 3.1 Do destination and time of day affect the accepted coffee house coupon rate?\n",
    "\n",
    "Overall, a higher number of drivers were presented with the coffee house coupon while en route to non-urgent destinations. Drivers are more likely to accept the coupon when driving to non-urgent places and more likely to reject it when driving to work or home. Among all accepted coffee house coupons, 63% were by drivers heading to non-urgent destinations.\n",
    "\n",
    "Upon analyzing the data based on destination and time of day, it is evident that drivers exhibit a higher likelihood of accepting the coffee house coupon when en route to non-urgent destinations at 10 a.m. and 2 p.m. Conversely, they are less inclined to accept the coupon during their morning commute to work or at 6 p.m.commute back home.\n",
    "\n",
    "#### 3.2 How does the weather and the time of the day affect coupon acceptance rate?\n",
    "\n",
    "As anticipated, the data indicates higher acceptance rates for coupons when the weather is sunny. However, for coffee house coupons, the time of day remains a critical decision factor. Overall, there is an increased number of accepted coupons on sunny days, with the proportion of accepted versus rejected coupons significantly favoring acceptance at 10 a.m. and 2 p.m. Additionally, the time of day is also a crucial factor in coupon acceptance on both snowy and rainy days.\n",
    "\n",
    "#### 4.1 What is the relationship between direction, coupon expiration, & acceptance rate? \n",
    "\n",
    "Regardless of direction, coupons that expire in one day are accepted more frequently than those that expire in two hours.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
