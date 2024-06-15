"""My non suspicious boring data retriever"""

import argparse
import json

import requests

endpoint = "https://hypernovatech-92292d4bbac0.herokuapp.com"
employees_route = "/employees"
employee_route = lambda employee: f"/employees/{employee}"

# DON'T FORGET
# username: jacobwhitman84
# password: mhw@ADfqbBwf_2dr@CtFa

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-id", required=True, type=str)
    args = parser.parse_args()
    session_id = args.session_id

    data = json.loads(
        requests.get(
            endpoint + employees_route,
            headers={"Authorization": f"Basic {session_id}"},
        ).content
    )
    if "employees" in data:
        employees = data["employees"]
    else:
        print(data)
        exit()

    for employee in employees:
        print(
            json.loads(
                requests.get(
                    endpoint + employee_route(employee),
                    headers={"Authorization": f"Basic {session_id}"},
                ).content
            )
        )
