import sys, os, argparse

print()
print("###### Build site pages ######");
print("PYTHON VERSION: " + ".".join(map(str, sys.version_info[:3])))
print("# Script call: " + " ".join(sys.argv) + "\n----------");

parser = argparse.ArgumentParser(description="Gets stats from a bunch of abyss assemblies.");
parser.add_argument("--all", dest="all", help="Build all pages", action="store_true", default=False);
parser.add_argument("--index", dest="index", help="Without --all: build index.html. With --all: exlude index.html", action="store_true", default=False);
parser.add_argument("--servers", dest="servers", help="Without --all: build servers.html. With --all: exlude servers.html", action="store_true", default=False);
parser.add_argument("--start", dest="start", help="Without --all: build start.html. With --all: exlude start.html", action="store_true", default=False);
parser.add_argument("--files", dest="files", help="Without --all: build files.html. With --all: exlude files.html", action="store_true", default=False);
parser.add_argument("--install", dest="install", help="Without --all: build install.html. With --all: exlude install.html", action="store_true", default=False);
parser.add_argument("--jobs", dest="jobs", help="Without --all: build jobs.html. With --all: exlude jobs.html", action="store_true", default=False);
parser.add_argument("--nodes", dest="nodes", help="Without --all: build nodes.html. With --all: exlude nodes.html", action="store_true", default=False);
parser.add_argument("--links", dest="links", help="Without --all: build links.html. With --all: exlude links.html", action="store_true", default=False);
args = parser.parse_args();
# Input options.

#cwd = os.getcwd();
os.chdir("generators");

pages = {
    'index' : args.index,
    'servers' : args.servers,
    'start' : args.start,
    'files' : args.files,
    'install' : args.install,
    'jobs' : args.jobs,
    'nodes' : args.nodes,
    'links' : args.links,
}

if args.all:
    pages = { page : False if pages[page] == True else True for page in pages };

if pages['index']:
    os.system("python index_generator.py");

if pages['servers']:
    os.system("python servers_generator.py");

if pages['start']:
    os.system("python start_generator.py");

if pages['files']:
    os.system("python files_generator.py");

if pages['install']:
    os.system("python install_generator.py");

if pages['jobs']:
    os.system("python jobs_generator.py");

if pages['nodes']:
    os.system("python nodes_generator.py");

if pages['links']:
    os.system("python links_generator.py");
    
print("----------\nDone!");


