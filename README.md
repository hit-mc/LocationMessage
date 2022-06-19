English | [中文](./README_zh.md)

# Location Message

## what is this?

This is a library that converts `position` into an `RTextList` in MCDR. Provide a unified interface for all services that need to broadcast or query location.

## interface prototype

````Python
def location_message(position: Position, dimension_str: str, name: Optional[str] = None, display_voxel: bool = True, display_xaero: bool = True, xaero_name: Optional[str] = None) -> RTextList
````

# Here

These codes come from the [Here](https://github.com/TISUnion/Here) plugin, which implements a very nice location prompt, but it is is coupled with this plugin.

This repository decouples the Here plugin.