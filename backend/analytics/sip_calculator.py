def sip_future_value(monthly_investment,
                     annual_return,
                     years):

    monthly_rate = annual_return / 12 / 100

    months = years * 12

    future_value = (
        monthly_investment *
        (((1 + monthly_rate) ** months - 1)
         / monthly_rate)
        * (1 + monthly_rate)
    )

    return round(future_value, 2)


if __name__ == "__main__":

    future_value = sip_future_value(
        monthly_investment=5000,
        annual_return=12,
        years=10
    )

    print("Future Value:", future_value)