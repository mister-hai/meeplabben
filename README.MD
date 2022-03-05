    LINKS/CREDITS ARE IN LICENSE, README IS FOR INFORMATION

# updates

    this is an updated work in progress, for a minimally functional 
    software, go to the previous repo in this github account

    https://github.com/mister-hai/sandboxy

    This new version will have kubernetes functionality and can be considered 
    a true "version 1", sandboxy should be considered a beta version that is now unsupported (until I get more helpers, I am busy IRL)
# PENTEST SANDBOX

    this is an all in one setup script for a docker/kubernetes cluster
    specifically, it creates a pentesting sandbox/ctfd instance

    now officially named 
    MEEPLABBEN

    because google translates it in dutch to

    PLAY ALONG

    and if you remove one letter at a time from labben
    meeplabben = play along
    meepabben  = contribute
    meepbben   = join in


# Table Of Contents

    until the start script is finished, this is the official documentation
    important data
    system prep
    KCTF INSTRUCTIONS
    NETWORK LAYOUT 
    There are two directories of concern

![terminal output](https://raw.githubusercontent.com/mister-hai/sandboxy/master/extra/docs/ctfd1.png)
![terminal output](https://raw.githubusercontent.com/mister-hai/sandboxy/master/extra/docs/test1.png)

![platform display](https://raw.githubusercontent.com/mister-hai/sandboxy/master/extra/docs/startscript.png))

# CTFCLI 
    to create an initial repository,you must structure it as the following

    repo folder
        named category folder
            challenge folder
                handout folder
                    handout file/s
                soution folder
                    solution file/s
                challenge.yaml

            If necessary, the following structure is needed for a deployment
            challenge folder
                challenge.yaml
                deployment folder
                    deployment.yaml
                    service.yaml
                    dockerfile
                handout folder
                    handout file/s
                soution folder
                    solution file/s

# kubernetes config

    kubernetes config information is loaded from the shell environment with the following code:

    ```python
    kube_config.load_kube_config(
        config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH),
        context=os.environ.get("KUBECONTEXT"),
    )
    ```
    to change the directory you must change the environment variable
    
    See here: https://github.com/kubernetes-incubator/client-python/blob/436351b027df2673869ee00e0ff5589e6b3e2b7d/kubernetes/config/kube_config.py#L283

    config.load_kube_config(context='some context')

    If you are not familiar with Kubernetes contexts, Kubernetes stores your configuration under ~/.kube/config (default location). In it you will find context definition for every cluster you may have access to. A field called current-context defines your current context.

    You can issue the following commands:
    
    kubectl config current-context to see the current context
    
    kubectl config view to view all the configuration

    The KUBECONFIG environment variable holds a list of kubeconfig files. 
    For Linux and Mac, the list is colon-delimited. 
    For Windows, the list is semicolon-delimited. 

    The KUBECONFIG environment variable is not required. 
    If the KUBECONFIG environment variable doesn't exist, 
    kubectl uses the default kubeconfig file, $HOME/.kube/config.

    If the KUBECONFIG environment variable does exist, 
    kubectl uses an effective configuration that is the result of 
    merging the files listed in the KUBECONFIG environment variable.
# PROGRESS

        ctfcli completely rewritten
        installer semi-functional
        ctfd server operational

        nginx proxy still not scrubbing port number from uri, I think this is a docker specific issue and I would appreciate assistance in the matter
## Important Information

        -sandboxy
            the docker-compose file directory containing the data created by
            CTFd and the users of the platform (mysql,cache,etc) to be packed 
            up and distributed to a replacment system in the event of a server change
            
            /containers
                contains the folders holding dockerfiles and resources for each Container

                /CTFd
                    Contains the build data for the ctfd docker container
                
                /nginx
                    ditto

            /data 
                where the portable data is placed (mysql/redis/ctfd/nginx/etc)

                /certbot/conf/live
                    This is where your certs are, keep an eye on this folder!

                /CTFd/Challenges
                    The challenge repository, managed by a rewrite of ctfcli

    the important files to start with for development are 
        - main-compose.yaml
        - haxnet.yaml
               
       The "containers" directory has each folder as a seperate docker box
       with its own dockerfile and everything necessary in that folder as 
       the build dir

        for linting/dev, you edit:
            /config/nginx_template.conf

        then you copy that to:
            /containers/nginx/nginx.conf.template

        finally, this file is where you set configuration parameters for the 
        environment:
            ./.env

        ! letsencrypt should be used only if a domain name is available !
                run init_letsencrypt.sh FIRST AND ONLY ONCE!
        ! letsencrypt should be used only if a domain name is available !

        haxnet.yaml is for severe sandboxing
        will contain
            debian cnc
            linux databases
            possibly windows hosts?
                must check legality

        all of them exploitable
    
    QUESTIONS FOR THE ADMIN:
        Can I install the following softwares:
            vagrant
            packer
            docker
            docker-compose
            kubernetes
            nsjail
            
        TODO:
            - add option to start.sh to include/build/init
                https://echoctf.red/
                https://github.com/echoCTF/echoCTF.RED
            
            - moar ctfd challenges here
                https://github.com/bsidessf

            - oohhh shiny!
                https://github.com/cliffe/SecGen

        we need more https://asmen.icopy.site/awesome/awesome-ctf/

        How to setup your public hostname for letsencrypt to function
            https://kerneltalks.com/howto/how-to-setup-domain-name-in-linux-server/
            https://raw.githubusercontent.com/wmnnd/nginx-certbot/master/init-letsencrypt.sh


# SYSTEMPREP

        Instructions for setting up a server from scratch can be found here

        extras/ServerSetup.MD

# certbot initiation
    
    Docker compose command before "docker-compose -f main-compose.yaml up"
    docker-compose -f main-compose.yaml run --rm -v "./data/certbot/conf:/etc/letsencrypt" -v "./data/certbot/www:/var/www/certbot" -v "./data/log/letsencrypt:/var/log/letsencrypt" nginx --entrypoint certbot --nginx --noninteractive --agree-tos --register-unsafely-without-email -d fightbiscuits.firewall-gateway.net 

# KCTF INSTRUCTIONS
    
    After installing kctf
    in a terminal, in the main project directory
    
        source kctf/activate

            - activates the kctf environment allowing you to upload
                challenge.yaml files from kubernetes deployments

        kctf cluster create local-cluster --start --type kind

            - creates a "kind" cluster, kind is a docker driver
                for kubernetes that has recently been deprecated
                although will remain supporteted as a containerd 
                abstraction
    
    FROM THE MAIN PROJECT DIRECTORY:
        perform the following sort of commands to move the kubernetes 
        challenges to the kctf templates folder
    
        cp -ar ./challengedir/UIUCTF-2021-Public/web/* ./kctf/challenge-templates/
        cp -ar ./challengedir/UIUCTF-2021-Public/pwn/* ./kctf/challenge-templates/

    Now you can create the challenges with kctf
    THE CHALLENGES MUST BE UPLOADED TO CTFD FIRST BEFORE ACTIVATING THE ENVIRONMENT
    This example uses ponydb from the UIUCTF-2021 challenge

        kctf chal create --template ponydb ponydb && cd ponydb
            - creates a folder in the main project directory, alongside kctf and 
                sandboxy and the main repository for CTFd
            - changes shell location to that challenge folder
            - the challenge is created from the template
    
    in that folder run the following command:
    
        kctf chal start

    And you will see the following as output:

        [*] building image in "/home/moop/pwnyide/challenge"
        [*] Image ID "8373-----49fe"
        [*] building image in "/home/moop/pwnyide/healthcheck"
        [*] Image ID "c0b07bb15de------36"
        Image: "kind/challenge:8373f7-----05549fe" with ID "sha256:8373f7b887b741ea-----549fe" not yet present on node "kctf-cluster-control-plane", loading...      
        [*] Image pushed to "kind/challenge:8373f7------549fe"
        Image: "kind/healthcheck:c0b07bb15----337a36" with ID "sha256:c0b----37a36" not yet present on node "kctf-cluster-control-plane", loading...
        [*] Image pushed to "kind/healthcheck:c0b07----337a36"
        challenge.kctf.dev/pwnyide created
    
    CONNECTING TO THE CHALLENGE:
    
    To connect to the challenge, run the following command:

        kctf chal debug port-forward &
    
    You will see the following output:

        moop@fightbiscuits:~/pwnyide$ kctf chal debug port-forward &
        [1] 131556
        moop@fightbiscuits:~/pwnyide$ [*] starting port-forward, ctrl+c to exit
        Forwarding from 127.0.0.1:42743 -> 1337

## Some Notes

    
    Historically the security of user namespace was uncertain. eg: lwn.net/Articles/673597 . 
    If a user, as root inside her own namespace can trick the kernel into allowing an operation
    on the real host, there's privilege escalation. Usual non-user namespaces require explicit
    root (so admin) permission and so run what the admin chose: that's a known risk. A later
    mechanism was added in vanilla kernel: user.max_user_namespaces . When set to 0 user
    namespaces are disabled. The Debian (actually from Ubuntu) patch is still around, even if
    probably obsolete. Maybe for compatibility reasons – A.B Mar 20 '18 at 14:30
	clear

