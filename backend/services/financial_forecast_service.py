# import math


# def calculate_sip_future_value(
#     monthly_investment,
#     annual_return,
#     years
# ):

#     monthly_rate = annual_return / 12 / 100

#     months = years * 12

#     future_value = (
#         monthly_investment
#         * (
#             ((1 + monthly_rate) ** months - 1)
#             / monthly_rate
#         )
#         * (1 + monthly_rate)
#     )

#     return round(future_value, 2)

# def inflation_adjusted_value(
#     future_value,
#     inflation_rate,
#     years
# ):

#     adjusted = (
#         future_value
#         / ((1 + inflation_rate / 100) ** years)
#     )

#     return round(adjusted, 2)


# if __name__ == "__main__":

#     corpus = calculate_sip_future_value(
#         monthly_investment=60000,
#         annual_return=14,
#         years=7
#     )

#     adjusted = inflation_adjusted_value(
#         corpus,
#         6,
#         7
#     )

# print("Future Corpus:", corpus)

# print("Inflation Adjusted:", adjusted)
# # print("Inflation Adjusted:", adjusted)
# # print("Inflation Adjusted:", adjusted)
# # print("Inflation Adjusted:", adjusted)

import math


def calculate_sip_future_value(
    monthly_investment,
    annual_return,
    years
):

    monthly_rate = annual_return / 12 / 100

    months = years * 12

    future_value = (
        monthly_investment
        * (
            ((1 + monthly_rate) ** months - 1)
            / monthly_rate
        )
        * (1 + monthly_rate)
    )

    return round(future_value, 2)


def inflation_adjusted_value(
    future_value,
    inflation_rate,
    years
):

    adjusted = (
        future_value
        / ((1 + inflation_rate / 100) ** years)
    )

    return round(adjusted, 2)


if __name__ == "__main__":

    corpus = calculate_sip_future_value(
        monthly_investment=60000,
        annual_return=14,
        years=7
    )

    adjusted = inflation_adjusted_value(
        corpus,
        6,
        7
    )

    print("Future Corpus:", corpus)

    print("Inflation Adjusted:", adjusted)

