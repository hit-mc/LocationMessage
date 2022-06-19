from typing import Optional

from mcdreforged.api.rtext import RText, RTextList, RColor, RAction, RTextBase

from location_message.dimension import get_dimension, Dimension, LegacyDimension
from location_message.position import Position


def coordinate_text(x: float, y: float, z: float, dimension: Dimension, click_to_teleport: bool = True) -> RTextBase:
    coord = RText('[{}, {}, {}]'.format(int(x), int(y), int(z)),
                  dimension.get_coordinate_color())
    if click_to_teleport:
        return (
            coord.h(dimension.get_rtext() + ': 点击以传送到' + coord.copy()).
            c(RAction.suggest_command, '/execute in {} run tp {} {} {}'.format(
                dimension.get_reg_key(), int(x), int(y), int(z)))
        )
    else:
        return coord.h(dimension.get_rtext())


def location_message(position: Position, dimension_str: str, name: Optional[str] = None, display_voxel: bool = True, display_xaero: bool = True, xaero_name: Optional[str] = None) -> RTextList:
    x, y, z = position
    dimension = get_dimension(dimension_str)
    texts = RTextList(dimension.get_rtext(), ' ',
                      coordinate_text(x, y, z, dimension))
    if name is not None:
        texts = RTextList(RText(name, RColor.yellow), ' @ ', texts)
    if display_voxel:
        texts.append(' ', RText('[+V]', RColor.aqua).h('§bVoxelmap§r: 点此以高亮坐标点, 或者Ctrl点击添加路径点').c(
            RAction.run_command, '/newWaypoint x:{}, y:{}, z:{}, dim:{}'.format(
                int(x), int(y), int(z), dimension.get_reg_key()
            )
        ))
    if display_xaero:
        if name:
            canonical_name = name[0]
        else:
            canonical_name = 'X'
        xaero_name = xaero_name or canonical_name
        command = "xaero_waypoint_add:{}:{}:{}:{}:{}:6:false:0".format(
            name, xaero_name, int(x), int(y), int(z))
        if isinstance(dimension, LegacyDimension):
            command += ':Internal_{}_waypoints'.format(
                dimension.get_reg_key().replace('minecraft:', '').strip())
        texts.append(' ',  RText(
            '[+X]', RColor.gold).h('§6Xaeros Minimap§r: 点击添加路径点').c(RAction.run_command, command))

    if dimension.has_opposite():
        oppo_dim, oppo_pos = dimension.get_opposite(position)
        arrow = RText('->', RColor.gray)
        texts.append(RText.format(
            ' {} {}',
            arrow.copy().h(RText.format('{} {} {}', dimension.get_rtext(), arrow, oppo_dim.get_rtext())),
            coordinate_text(oppo_pos.x, oppo_pos.y, oppo_pos.z, oppo_dim)
        ))

    return texts
