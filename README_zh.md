[English](./README.md) | 中文

# Location Message

## 这是什么？

这是一个库，将`位置`，转化为一个MCDR中的`RTextList`。为所有的，需要广播或查询位置的服务提供统一的接口。

## 接口原型

```Python
def location_message(position: Position, dimension_str: str, name: Optional[str] = None, display_voxel: bool = True, display_xaero: bool = True, xaero_name: Optional[str] = None) -> RTextList
```

# Here

这些代码来源于[Here](https://github.com/TISUnion/Here)插件，这个插件实现了非常漂亮的位置服务提示，然而位置信息和这个插件是耦合的。

这个仓库将解耦了Here插件。