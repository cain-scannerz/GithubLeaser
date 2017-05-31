# Function for reading the github API response and getting the required field
function jsonval {
   temp=`echo $json | sed 's/\\\\\//\//g' | sed 's/[{}]//g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' | sed 's/\"\:\"/\|/g' | sed 's/[\,]/ /g' | sed 's/\"//g' | grep -w "tarball_url"`
    echo ${temp##*|}
}

# Check the latest release, get the tarball_url & the version 
json=`curl -s GET https://api.github.com/repos/DirectoryLister/DirectoryLister/releases/latest`
picurl=`jsonval`
IFS='/v' read -a array <<< $picurl

# Check if we already have the directory. If we do we exit the script
pwd
pwd [options]
fp=$(pwd)
if [[ -d "$fp/current/web/${array[-1]}" && ! -L "$fp/current/web/${array[-1]}" ]] ; then
    echo "Directory already exists."
    exit 0
fi

# Get the tar and untar it into our new directory
putIn=`curl -L https://api.github.com/repos/DirectoryLister/DirectoryLister/tarball/${array[-1]} | tar xz --strip=1 -C current/web/${array[-1]}`

echo "Successfully Updated Version"
