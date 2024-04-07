# packages =  "{\"deps\":[{\"name\":\"net.sf.sojo:sojo\",\"version\":\"1.0.13\",\"ecosystem\":\"Maven\"},{\"name\":\"net.sourceforge.plantuml:plantuml-mit\",\"version\":\"1.2023.7\",\"ecosystem\":\"Maven\"},{\"name\":\"com.owlike:genson\",\"version\":\"0.94\",\"ecosystem\":\"Maven\"},{\"name\":\"org.xerial.snappy:snappy-java\",\"version\":\"1.0.3\",\"ecosystem\":\"Maven\"},{\"name\":\"uap-core\",\"version\":\"1.0.1\",\"ecosystem\":\"npm\"}]}"

# - Given the list of open source package dependencies above, query the following API to retrieve vulnerability information on the dependencies (https://google.github.io/osv.dev/post-v1-query/).

# - Using the relevant CVE information returned on the packages, store this information in a CSV file using the following format:

# ID,Summary,CVE(aliases),severity,published,package name(affected.package.name), ecosystem (affected.package.ecosystem)

# The names in parenthesis represents how the data is nested within the JSON response from the API for convenience.

# - Write two functions that will return results from the CSV file just written
# - Function1 - parse the results and return the oldest CVE when given the ecosystem is passed as a parameter
# - Function2 - parse the results and return the highest severity CVE (Critical, High, Medium, Low). If there are multiple CVE's that match the highest severity, return the oldest depending on when that CVE was published

import requests
import json
import csv
import gc

packages =  "{\"deps\":[{\"name\":\"net.sf.sojo:sojo\",\"version\":\"1.0.13\",\"ecosystem\":\"Maven\"},{\"name\":\"net.sourceforge.plantuml:plantuml-mit\",\"version\":\"1.2023.7\",\"ecosystem\":\"Maven\"},{\"name\":\"com.owlike:genson\",\"version\":\"0.94\",\"ecosystem\":\"Maven\"},{\"name\":\"org.xerial.snappy:snappy-java\",\"version\":\"1.0.3\",\"ecosystem\":\"Maven\"},{\"name\":\"uap-core\",\"version\":\"1.0.1\",\"ecosystem\":\"npm\"}]}"

packages_details = json.loads(packages)["deps"]
headers = ["ID","Summary","alias","severity","published","package_name","ecosystem"]
print(len(gc.get_objects()))
with open("result.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for dep in packages_details:
            name = dep["name"]
            version = dep["version"]
            # data parameter should be a string
            response = requests.post("https://api.osv.dev/v1/query",data='{"package":{"name":"'+name+'"},"version":"'+version+'"}')
            
            obj = response.json()# type of obj is str

            if obj.keys():
                vulns = obj["vulns"][0]
                id = vulns["id"]
                Summary = vulns["summary"]
                alias = vulns["aliases"]
                severity = vulns["database_specific"]["severity"]
                published = vulns["published"]
                package_name = vulns["affected"][0]["package"]["name"]
                ecosystem = vulns["affected"][0]["package"]["ecosystem"]

                writer.writerow([id,Summary,alias,severity,published,package_name,ecosystem])
gc.collect()
print(len(gc.get_objects()))


with open("result.csv", "r") as readFile:
     lines = readFile.readlines()
     for line in lines:
        print(type(line))