from langserve import RemoteRunnable

remoteChain = RemoteRunnable("http://localhost:8000/translate")
textResult = remoteChain.invoke({"idiom": "francês", "text": "Se inscreva no canal para aprender Python"})

print(textResult)

# This is the way that we need to invoke the functionality developed here in other mappings, if required.
# For example if we have a trip software which helps people on travelling related themes, we can use this translater AI program to help them somehow, in terms of translation.