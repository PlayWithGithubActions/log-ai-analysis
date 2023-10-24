import argparse
import google.generativeai as palm


def get_fix(path, apikey, promptkey):

    # required prompt
    prompt = promptkey
    palm.configure(api_key=apikey)

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    try:
        with open(path, 'r') as file:
            prompt += "\nAnalyze the following content:\n" + file.read()
            file.close()
            ans = palm.generate_text(model=model, prompt=prompt,
                 temperature=0, max_output_tokens=800)
            print(ans.candidates[0]['output'])
    except FileNotFoundError:
        print("Unable to find specified file. Use pwd for referrence.")


parser = argparse.ArgumentParser(description="Get file name")
parser.add_argument('filename')
parser.add_argument('apikey')
parser.add_argument('promptkey')
# Arguments
args = parser.parse_args()
print(args.filename)
print(args.apikey)
print(args.promptkey)
get_fix(args.filename, args.apikey,args.promptkey)
