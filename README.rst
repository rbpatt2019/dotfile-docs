Slaying Dragons with Nix
########################

It's always there, in the far corners of the early maps [#maps]_:

    Here be dragons.

Uncharted regions where travelers dare to tread. From very early on, my dotfiles have
felt the same to me. Namely, not as well maintained as they should be because trying
to keep them up-to-date across multiple machines running different OS's was a
first-rate nightmare. Recently, I realised that this needed to change. I began
researching different ways to fix this, and came across `Nix`_. I was put off at first.
It seemed an overly heavy and complex system for what I wanted to achieve, a bit like
driving a small nail with a sledgehammer. Several months later, as I coaxed `MacPorts`_
through another OS update, it all clicked. I went back to `Nix` and was immediately in
love. I'm now convinced this tool is how St. George slayed the dragon [#stg]_.

.. [#maps] {-} No, seriously, this really happened! Well, at least `once`_...
.. [#stg] {-} Clearly, `Dragon Hill`_ is an ancient terminal that George used to install Nix.

.. _Nix: https://nixos.org/
.. _MacPorts: https://www.macports.org/
.. _once: https://en.wikipedia.org/wiki/Hunt%E2%80%93Lenox_Globe
.. _Dragon Hill: https://en.wikipedia.org/wiki/Dragon_Hill,_Uffington

So why this project?
====================

Though it has improved by leaps and bounds recently, the documentaion about `nix` has
been historically lacking. I found myself struggling for answers on many points,
trolling through old forums and threads to glean what information I could. To help
myself remeber, I started keeping notes. Eventually, I realised that I should track
them with `git`, so I don't lose them. Which lead to me concluding that I should write
them up properly, in case other could benefit. So come along as we explore the
delightful, and occassionally mind-numbingly frustrating, world of reproducible dotfiles
with `nix`.
