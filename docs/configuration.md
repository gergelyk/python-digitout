# Configuration

## Default Configuration

If you call `digitout()` with your target as the only parameter and pipe the results to another process (TTY unavailable), default configuration will be used. It matches every object met while traversing. Visitors used for traversing are set up according to the common sense.

## Ad Hoc Configuration

When TTY is available, calling `digitout()` with your target as the only parameter will open an interactive interface where you can specify how memory should be traversed and what we are searching for. Configuration can be assigend to a name and reused later. Configurations are stored under `~/.config/digitout/configs`[^1].

## A Priori Configuration

If TTY is not available, but you are not satisfied with default configuration, you can use one of the custom configurations, buy passing its name to `digitout()`. E.g.:

```python
import digitout
digitout(mytarget, config='myconfig')
```

Configurations can be edited interactively by invoking:

```sh
python -m digitout
```

## Fixed Configuration

Finally there is an option of passing configuration as a dictionary. The best way is to initialize dictionary with default values and modify them later. E.g.:

```
import digitout
from digitout import make_default_config
config = make_default_config()
config['match']['expression'] = 'lambda value: value == 123'
digitout(mytarget, config)
```

[^1]: With default [XDG](https://www.freedesktop.org/wiki/Software/xdg-utils/) settings.
