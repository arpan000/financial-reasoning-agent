def generate_portfolio_allocation(

    risk_profile
):

    if risk_profile == "aggressive":

        return {

            "large_cap": 40,

            "mid_cap": 30,

            "small_cap": 20,

            "debt": 10
        }

    elif risk_profile == "moderate":

        return {

            "large_cap": 40,

            "mid_cap": 20,

            "small_cap": 10,

            "debt": 30
        }

    else:

        return {

            "large_cap": 30,

            "mid_cap": 10,

            "small_cap": 0,

            "debt": 60
        }


if __name__ == "__main__":

    result = generate_portfolio_allocation(
        "aggressive"
    )

    print(result)