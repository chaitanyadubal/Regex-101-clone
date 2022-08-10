from flask import Flask, render_template, request
import re 

app = Flask(__name__)

############################################

@app.route('/',methods=["POST","GET"])
def index_function():
    #print (request.__dict__)
    res=" "
    try:
        regex = request.form['expression']
        test_str = request.form['find_string']
        matches = re.finditer(regex, test_str, re.MULTILINE)
        


        for matchNum, match in enumerate(matches, start=1):
            res="Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
            #print(res)
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                res="Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum))
                #print (res)
        return render_template('index.html',res=res)
    except:
        return render_template('index.html',res=res)



############################################

if __name__ == '__main__':
    app.run(debug=True)