# mistral

[![Build Status](https://travis-ci.org/mechanoid/mistral.svg?branch=master)](https://travis-ci.org/mechanoid/mistral)

convention driven easy to use module bundling based on rollup.

This project tries to help setting up frontend projects that have a need
for bundling business modules to separate bundles, while sharing libraries
as externals that are bundles themselves.

Consider a project structure, where you want to develop a list of
libraries that should be divided in technical modules, so that
their maintenance keeps structured and well organized.

To expose the libraries in a well structured way each of it is bundled
to a module containing its business logic. This means that any internal
libraries are removed from any outer access, which makes the libraries
more self contained and robust and it keeps the coupling low.
