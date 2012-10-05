#!/bin/bash -e

echo "------------------------------------------------------------"
echo "|   Install openzwave in tmp                               |"
echo "------------------------------------------------------------"
python setup.py install --root=build/tmp

cd docs
rm -Rf _build
echo "-----------------------------------------------------------------"
echo "|   Generate html docs                                          |"
echo "-----------------------------------------------------------------"
make html

echo "-----------------------------------------------------------------"
echo "|   Generate joomla docs                                        |"
echo "-----------------------------------------------------------------"
make joomla
cd ..
