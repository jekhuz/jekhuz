import requests, json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
nameid = "jekhuz"
repoid = "jekhuz"
yamlid = "build_and_release"
f = open("./README.md", "w")
pokemon_id = random.randint(1, 151)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''<p align="center">
    <img src="{result['sprites']['front_default']}" width="150" height="150">
</p>
<h3 align="center">You have been greeted by a wild <b>{result['name'].title()}</b></h3>

<a href="https://github.com/{nameid}"><h3 align="center"><b>{nameid}</b></h3></a>

<h3 align="center">Have a nice day!</h3>

<p align="center">

  <a href="https://github.com/{nameid}">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username={nameid}&hide=issues&hide_title=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff" />
   </a>
   
#### This Page Create at:

```bash
	
{timestr}

```

#### Create By Machine:

```bash

Host Name : {socket.gethostname()}

platform  : {platform.platform()}

Ip Local  : {socket.gethostbyname(socket.gethostname())}

```

[![LICENSE](https://img.shields.io/github/license/{nameid}/{repoid}.svg?style=flat-square&label=LICENSE)](https://github.com/{nameid}/{repoid}/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/{nameid}/{repoid}.svg?style=flat-square&label=Stars&logo=github)](https://github.com/{nameid}/{repoid}/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/{nameid}/{repoid}.svg?style=flat-square&label=Forks&logo=github)](https://github.com/{nameid}/{repoid}/forkingers)
[![build_firmware](https://github.com/{nameid}/{repoid}/actions/workflows/generate_readme.yml/badge.svg)](https://github.com/{nameid}/{repoid}/actions/workflows/generate_readme.yml) [![{yamlid}](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml/badge.svg)](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml)

#### Download This code Here:

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{nameid}/{repoid}?style=for-the-badge&label=Download)](https://github.com/{nameid}/{repoid}/releases) 

</p> 

#### About Me :

```bash

{nameid}

```

''')
f.close()
