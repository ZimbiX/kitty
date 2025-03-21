import termios
from ctypes import Array, c_ubyte
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    NewType,
    Optional,
    Tuple,
    TypedDict,
    Union,
)

from kitty.boss import Boss
from kitty.fonts import FontFeature
from kitty.fonts.render import FontObject
from kitty.marks import MarkerFunc
from kitty.options.types import Options
from kitty.types import SignalInfo

# Constants {{{
GLFW_PRIMARY_SELECTION: int
GLFW_CLIPBOARD: int
CLD_KILLED: int
CLD_STOPPED: int
CLD_CONTINUED: int
CLD_EXITED: int
SHM_NAME_MAX: int
MOUSE_SELECTION_LINE: int
MOUSE_SELECTION_EXTEND: int
MOUSE_SELECTION_NORMAL: int
MOUSE_SELECTION_WORD: int
MOUSE_SELECTION_RECTANGLE: int
MOUSE_SELECTION_LINE_FROM_POINT: int
MOUSE_SELECTION_MOVE_END: int
KITTY_VCS_REV: str
NO_CLOSE_REQUESTED: int
IMPERATIVE_CLOSE_REQUESTED: int
CLOSE_BEING_CONFIRMED: int
ERROR_PREFIX: str
GLSL_VERSION: int
GLFW_IBEAM_CURSOR: int
# start glfw functional keys (auto generated by gen-key-constants.py do not edit)
GLFW_FKEY_ESCAPE: int
GLFW_FKEY_ENTER: int
GLFW_FKEY_TAB: int
GLFW_FKEY_BACKSPACE: int
GLFW_FKEY_INSERT: int
GLFW_FKEY_DELETE: int
GLFW_FKEY_LEFT: int
GLFW_FKEY_RIGHT: int
GLFW_FKEY_UP: int
GLFW_FKEY_DOWN: int
GLFW_FKEY_PAGE_UP: int
GLFW_FKEY_PAGE_DOWN: int
GLFW_FKEY_HOME: int
GLFW_FKEY_END: int
GLFW_FKEY_CAPS_LOCK: int
GLFW_FKEY_SCROLL_LOCK: int
GLFW_FKEY_NUM_LOCK: int
GLFW_FKEY_PRINT_SCREEN: int
GLFW_FKEY_PAUSE: int
GLFW_FKEY_MENU: int
GLFW_FKEY_F1: int
GLFW_FKEY_F2: int
GLFW_FKEY_F3: int
GLFW_FKEY_F4: int
GLFW_FKEY_F5: int
GLFW_FKEY_F6: int
GLFW_FKEY_F7: int
GLFW_FKEY_F8: int
GLFW_FKEY_F9: int
GLFW_FKEY_F10: int
GLFW_FKEY_F11: int
GLFW_FKEY_F12: int
GLFW_FKEY_F13: int
GLFW_FKEY_F14: int
GLFW_FKEY_F15: int
GLFW_FKEY_F16: int
GLFW_FKEY_F17: int
GLFW_FKEY_F18: int
GLFW_FKEY_F19: int
GLFW_FKEY_F20: int
GLFW_FKEY_F21: int
GLFW_FKEY_F22: int
GLFW_FKEY_F23: int
GLFW_FKEY_F24: int
GLFW_FKEY_F25: int
GLFW_FKEY_F26: int
GLFW_FKEY_F27: int
GLFW_FKEY_F28: int
GLFW_FKEY_F29: int
GLFW_FKEY_F30: int
GLFW_FKEY_F31: int
GLFW_FKEY_F32: int
GLFW_FKEY_F33: int
GLFW_FKEY_F34: int
GLFW_FKEY_F35: int
GLFW_FKEY_KP_0: int
GLFW_FKEY_KP_1: int
GLFW_FKEY_KP_2: int
GLFW_FKEY_KP_3: int
GLFW_FKEY_KP_4: int
GLFW_FKEY_KP_5: int
GLFW_FKEY_KP_6: int
GLFW_FKEY_KP_7: int
GLFW_FKEY_KP_8: int
GLFW_FKEY_KP_9: int
GLFW_FKEY_KP_DECIMAL: int
GLFW_FKEY_KP_DIVIDE: int
GLFW_FKEY_KP_MULTIPLY: int
GLFW_FKEY_KP_SUBTRACT: int
GLFW_FKEY_KP_ADD: int
GLFW_FKEY_KP_ENTER: int
GLFW_FKEY_KP_EQUAL: int
GLFW_FKEY_KP_SEPARATOR: int
GLFW_FKEY_KP_LEFT: int
GLFW_FKEY_KP_RIGHT: int
GLFW_FKEY_KP_UP: int
GLFW_FKEY_KP_DOWN: int
GLFW_FKEY_KP_PAGE_UP: int
GLFW_FKEY_KP_PAGE_DOWN: int
GLFW_FKEY_KP_HOME: int
GLFW_FKEY_KP_END: int
GLFW_FKEY_KP_INSERT: int
GLFW_FKEY_KP_DELETE: int
GLFW_FKEY_KP_BEGIN: int
GLFW_FKEY_MEDIA_PLAY: int
GLFW_FKEY_MEDIA_PAUSE: int
GLFW_FKEY_MEDIA_PLAY_PAUSE: int
GLFW_FKEY_MEDIA_REVERSE: int
GLFW_FKEY_MEDIA_STOP: int
GLFW_FKEY_MEDIA_FAST_FORWARD: int
GLFW_FKEY_MEDIA_REWIND: int
GLFW_FKEY_MEDIA_TRACK_NEXT: int
GLFW_FKEY_MEDIA_TRACK_PREVIOUS: int
GLFW_FKEY_MEDIA_RECORD: int
GLFW_FKEY_LOWER_VOLUME: int
GLFW_FKEY_RAISE_VOLUME: int
GLFW_FKEY_MUTE_VOLUME: int
GLFW_FKEY_LEFT_SHIFT: int
GLFW_FKEY_LEFT_CONTROL: int
GLFW_FKEY_LEFT_ALT: int
GLFW_FKEY_LEFT_SUPER: int
GLFW_FKEY_LEFT_HYPER: int
GLFW_FKEY_LEFT_META: int
GLFW_FKEY_RIGHT_SHIFT: int
GLFW_FKEY_RIGHT_CONTROL: int
GLFW_FKEY_RIGHT_ALT: int
GLFW_FKEY_RIGHT_SUPER: int
GLFW_FKEY_RIGHT_HYPER: int
GLFW_FKEY_RIGHT_META: int
GLFW_FKEY_ISO_LEVEL3_SHIFT: int
GLFW_FKEY_ISO_LEVEL5_SHIFT: int
# end glfw functional keys
GLFW_MOD_SHIFT: int
GLFW_MOD_CONTROL: int
GLFW_MOD_ALT: int
GLFW_MOD_SUPER: int
GLFW_MOD_HYPER: int
GLFW_MOD_META: int
GLFW_MOD_CAPS_LOCK: int
GLFW_MOD_NUM_LOCK: int
GLFW_MOD_KITTY: int
GLFW_MOUSE_BUTTON_1: int
GLFW_MOUSE_BUTTON_2: int
GLFW_MOUSE_BUTTON_3: int
GLFW_MOUSE_BUTTON_4: int
GLFW_MOUSE_BUTTON_5: int
GLFW_MOUSE_BUTTON_6: int
GLFW_MOUSE_BUTTON_7: int
GLFW_MOUSE_BUTTON_8: int
GLFW_MOUSE_BUTTON_LAST: int
GLFW_MOUSE_BUTTON_LEFT: int
GLFW_MOUSE_BUTTON_RIGHT: int
GLFW_MOUSE_BUTTON_MIDDLE: int
GLFW_JOYSTICK_1: int
GLFW_JOYSTICK_2: int
GLFW_JOYSTICK_3: int
GLFW_JOYSTICK_4: int
GLFW_JOYSTICK_5: int
GLFW_JOYSTICK_6: int
GLFW_JOYSTICK_7: int
GLFW_JOYSTICK_8: int
GLFW_JOYSTICK_9: int
GLFW_JOYSTICK_10: int
GLFW_JOYSTICK_11: int
GLFW_JOYSTICK_12: int
GLFW_JOYSTICK_13: int
GLFW_JOYSTICK_14: int
GLFW_JOYSTICK_15: int
GLFW_JOYSTICK_16: int
GLFW_JOYSTICK_LAST: int
GLFW_NOT_INITIALIZED: int
GLFW_NO_CURRENT_CONTEXT: int
GLFW_INVALID_ENUM: int
GLFW_INVALID_VALUE: int
GLFW_OUT_OF_MEMORY: int
GLFW_API_UNAVAILABLE: int
GLFW_VERSION_UNAVAILABLE: int
GLFW_PLATFORM_ERROR: int
GLFW_FORMAT_UNAVAILABLE: int
GLFW_FOCUSED: int
GLFW_ICONIFIED: int
GLFW_RESIZABLE: int
GLFW_VISIBLE: int
GLFW_DECORATED: int
GLFW_AUTO_ICONIFY: int
GLFW_FLOATING: int
GLFW_RED_BITS: int
GLFW_GREEN_BITS: int
GLFW_BLUE_BITS: int
GLFW_ALPHA_BITS: int
GLFW_DEPTH_BITS: int
GLFW_STENCIL_BITS: int
GLFW_ACCUM_RED_BITS: int
GLFW_ACCUM_GREEN_BITS: int
GLFW_ACCUM_BLUE_BITS: int
GLFW_ACCUM_ALPHA_BITS: int
GLFW_AUX_BUFFERS: int
GLFW_STEREO: int
GLFW_SAMPLES: int
GLFW_SRGB_CAPABLE: int
GLFW_REFRESH_RATE: int
GLFW_DOUBLEBUFFER: int
GLFW_CLIENT_API: int
GLFW_CONTEXT_VERSION_MAJOR: int
GLFW_CONTEXT_VERSION_MINOR: int
GLFW_CONTEXT_REVISION: int
GLFW_CONTEXT_ROBUSTNESS: int
GLFW_OPENGL_FORWARD_COMPAT: int
GLFW_CONTEXT_DEBUG: int
GLFW_OPENGL_PROFILE: int
GLFW_OPENGL_API: int
GLFW_OPENGL_ES_API: int
GLFW_NO_ROBUSTNESS: int
GLFW_NO_RESET_NOTIFICATION: int
GLFW_LOSE_CONTEXT_ON_RESET: int
GLFW_OPENGL_ANY_PROFILE: int
GLFW_OPENGL_CORE_PROFILE: int
GLFW_OPENGL_COMPAT_PROFILE: int
GLFW_CURSOR: int
GLFW_STICKY_KEYS: int
GLFW_STICKY_MOUSE_BUTTONS: int
GLFW_CURSOR_NORMAL: int
GLFW_CURSOR_HIDDEN: int
GLFW_CURSOR_DISABLED: int
GLFW_CONNECTED: int
GLFW_DISCONNECTED: int
GLFW_PRESS: int
GLFW_RELEASE: int
GLFW_REPEAT: int
CURSOR_BEAM: int
CURSOR_BLOCK: int
NO_CURSOR_SHAPE: int
CURSOR_UNDERLINE: int
DECAWM: int
BGIMAGE_PROGRAM: int
BLIT_PROGRAM: int
CELL_BG_PROGRAM: int
CELL_FG_PROGRAM: int
CELL_PROGRAM: int
CELL_SPECIAL_PROGRAM: int
CSI: int
DCS: int
DECORATION: int
DIM: int
GRAPHICS_ALPHA_MASK_PROGRAM: int
GRAPHICS_PREMULT_PROGRAM: int
GRAPHICS_PROGRAM: int
MARK: int
MARK_MASK: int
DECORATION_MASK: int
NUM_UNDERLINE_STYLES: int
OSC: int
FILE_TRANSFER_CODE: int
REVERSE: int
SCROLL_FULL: int
SCROLL_LINE: int
SCROLL_PAGE: int
STRIKETHROUGH: int
TINT_PROGRAM: int
FC_MONO: int = 100
FC_DUAL: int
FC_WEIGHT_REGULAR: int
FC_WEIGHT_BOLD: int
FC_WIDTH_NORMAL: int
FC_SLANT_ROMAN: int
FC_SLANT_ITALIC: int
BORDERS_PROGRAM: int
PRESS: int
RELEASE: int
DRAG: int
MOVE: int
# }}}


def encode_key_for_tty(
    key: int = 0,
    shifted_key: int = 0,
    alternate_key: int = 0,
    mods: int = 0,
    action: int = 1,
    key_encoding_flags: int = 0,
    text: str = "",
    cursor_key_mode: bool = False
) -> str:
    pass


def log_error_string(s: str) -> None:
    pass


def redirect_std_streams(devnull: str) -> None:
    pass


def glfw_get_key_name(key: int, native_key: int) -> Optional[str]:
    pass


StartupCtx = NewType('StartupCtx', int)
Display = NewType('Display', int)


def init_x11_startup_notification(
    display: Display,
    window_id: int,
    startup_id: Optional[str] = None
) -> StartupCtx:
    pass


def end_x11_startup_notification(ctx: StartupCtx) -> None:
    pass


def x11_display() -> Optional[Display]:
    pass


def user_cache_dir() -> str:
    pass


def process_group_map() -> Tuple[Tuple[int, int], ...]:
    pass


def environ_of_process(pid: int) -> str:
    pass


def cmdline_of_process(pid: int) -> List[str]:
    pass


def cwd_of_process(pid: int) -> str:
    pass


def default_color_table() -> Tuple[int, ...]:
    pass


class FontConfigPattern(TypedDict):
    path: str
    index: int
    family: str
    full_name: str
    postscript_name: str
    style: str
    spacing: str
    fontfeatures: List[str]
    weight: int
    width: int
    slant: int
    hint_style: int
    subpixel: int
    lcdfilter: int
    hinting: bool
    scalable: bool
    outline: bool
    color: bool


def fc_list(
    spacing: int = -1,
    allow_bitmapped_fonts: bool = False
) -> Tuple[FontConfigPattern, ...]:
    pass


def fc_match(
    family: Optional[str] = None,
    bold: bool = False,
    italic: bool = False,
    spacing: int = FC_MONO,
    allow_bitmapped_fonts: bool = False,
    size_in_pts: float = 0.,
    dpi: float = 0.
) -> FontConfigPattern:
    pass


def fc_match_postscript_name(
    postscript_name: str
) -> FontConfigPattern:
    pass


class CoreTextFont(TypedDict):
    path: str
    postscript_name: str
    family: str
    style: str
    bold: bool
    italic: bool
    expanded: bool
    condensed: bool
    color_glyphs: bool
    monospace: bool
    weight: float
    width: float
    traits: int


def coretext_all_fonts() -> Tuple[CoreTextFont, ...]:
    pass


def add_timer(
    callback: Callable[[Optional[int]], None],
    interval: float,
    repeats: bool = True
) -> int:
    pass


def remove_timer(timer_id: int) -> None:
    pass


def monitor_pid(pid: int) -> None:
    pass


def add_window(os_window_id: int, tab_id: int, title: str) -> int:
    pass


def compile_program(
    which: int, vertex_shader: str, fragment_shader: str
) -> int:
    pass


def init_cell_program() -> None:
    pass


def set_titlebar_color(os_window_id: int, color: int, use_system_color: bool = False, system_color: int = 0) -> bool:
    pass


def add_borders_rect(
    os_window_id: int, tab_id: int, left: int, top: int, right: int,
    bottom: int, color: int
) -> None:
    pass


def init_borders_program() -> None:
    pass


def os_window_has_background_image(os_window_id: int) -> bool:
    pass


def dbus_send_notification(
    app_name: str,
    icon: str,
    summary: str,
    body: str,
    action_name: str,
    timeout: int = -1
) -> int:
    pass


def cocoa_send_notification(
    identifier: Optional[str],
    title: str,
    body: Optional[str],
    subtitle: Optional[str],
) -> None:
    pass


def create_os_window(
    get_window_size: Callable[[int, int, int, int, float, float], Tuple[int,
                                                                        int]],
    pre_show_callback: Callable[[int], None],
    title: str,
    wm_class_name: str,
    wm_class_class: str,
    load_programs: Optional[Callable[[bool], None]] = None,
    x: int = -1,
    y: int = -1,
    disallow_override_title: bool = False,
) -> int:
    pass


def update_window_title(
    os_window_id: int, tab_id: int, window_id: int, title: str
) -> None:
    pass


def update_window_visibility(
    os_window_id: int, tab_id: int, window_id: int,
    visible: bool
) -> None:
    pass


def sync_os_window_title(os_window_id: int) -> None:
    pass


def set_options(
    opts: Optional[Options],
    is_wayland: bool = False,
    debug_rendering: bool = False,
    debug_font_fallback: bool = False
) -> None:
    pass


def get_options() -> Options:
    pass


def parse_font_feature(ff: str) -> bytes:
    pass


def glfw_primary_monitor_size() -> Tuple[int, int]:
    pass


def set_default_window_icon(path: str) -> None:
    pass


def set_custom_cursor(
    cursor_type: int,
    images: Tuple[Tuple[bytes, int, int], ...],
    x: int = 0,
    y: int = 0
) -> None:
    pass


def load_png_data(data: bytes) -> Tuple[bytes, int, int]:
    pass


def glfw_terminate() -> None:
    pass


def glfw_init(path: str, debug_keyboard: bool = False, debug_rendering: bool = False) -> bool:
    pass


def free_font_data() -> None:
    pass


def toggle_maximized(os_window_id: int = 0) -> bool:
    pass


def toggle_fullscreen(os_window_id: int = 0) -> bool:
    pass


def thread_write(fd: int, data: bytes) -> None:
    pass


def set_in_sequence_mode(yes: bool) -> None:
    pass


def set_background_image(
    path: Optional[str],
    os_window_ids: Tuple[int, ...],
    configured: bool = True,
    layout_name: Optional[str] = None,
) -> None:
    pass


def set_boss(boss: Boss) -> None:
    pass


def get_boss() -> Boss:  # this can return None but we ignore that for convenience
    pass


def safe_pipe(nonblock: bool = True) -> Tuple[int, int]:
    pass


def patch_global_colors(spec: Dict[str, Optional[int]], configured: bool) -> None:
    pass


class Color:
    @property
    def rgb(self) -> int:
        pass

    @property
    def red(self) -> int:
        pass
    r = red

    @property
    def green(self) -> int:
        pass
    g = green

    @property
    def blue(self) -> int:
        pass
    b = blue

    @property
    def alpha(self) -> int:
        pass
    a = alpha

    @property
    def luminance(self) -> float:
        pass

    @property
    def as_sgr(self) -> str:
        pass

    @property
    def as_sharp(self) -> str:
        pass

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: int = 0) -> None:
        pass

    def __truediv__(self, divisor: float) -> Tuple[float, float, float, float]:  # (r, g, b, a)
        pass

    def __int__(self) -> int:
        pass

    def __hash__(self) -> int:
        pass

    def __eq__(self, other: Any) -> bool:
        pass

    def __ne__(self, other: Any) -> bool:
        pass

    def contrast(self, other: 'Color') -> float:
        pass


class ColorProfile:

    default_bg: int

    def as_dict(self) -> Dict[str, Optional[int]]:
        pass

    def as_color(self, val: int) -> Optional[Color]:
        pass

    def set_color(self, num: int, val: int) -> None:
        pass

    def reset_color_table(self) -> None:
        pass

    def reset_color(self, num: int) -> None:
        pass

    def update_ansi_color_table(self, val: int) -> None:
        pass

    def set_configured_colors(
        self, fg: int, bg: int, cursor: int = 0, cursor_text: int = 0, highlight_fg: int = 0, highlight_bg: int = 0, visual_bell_color: int = 0
    ) -> None:
        pass


def patch_color_profiles(
    spec: Dict[str, Optional[int]], profiles: Tuple[ColorProfile, ...], change_configured: bool
) -> None:
    pass


def create_canvas(d: bytes, w: int, x: int, y: int, cw: int, ch: int, bpp: int) -> bytes: ...


def os_window_font_size(
    os_window_id: int, new_sz: float = -1., force: bool = False
) -> float:
    pass


def cocoa_set_notification_activated_callback(identifier: Optional[Callable[[str], None]]) -> None:
    pass


def cocoa_set_global_shortcut(name: str, mods: int, key: int) -> bool:
    pass


def cocoa_get_lang() -> Optional[str]:
    pass


def cocoa_set_url_handler(url_scheme: str, bundle_id: Optional[str] = None) -> None:
    pass


def cocoa_set_app_icon(icon_path: str, app_path: Optional[str] = None) -> None:
    pass


def cocoa_set_dock_icon(icon_path: str) -> None:
    pass


def cocoa_hide_app() -> None:
    pass


def cocoa_hide_other_apps() -> None:
    pass


def cocoa_minimize_os_window(os_window_id: Optional[int] = None) -> None:
    pass


def locale_is_valid(name: str) -> bool:
    pass


def mark_os_window_for_close(os_window_id: int, cr_type: int = 2) -> bool:
    pass


def set_application_quit_request(cr_type: int = 2) -> None:
    pass


def current_application_quit_request() -> int:
    pass


def global_font_size(val: float = -1.) -> float:
    pass


def focus_os_window(os_window_id: int, also_raise: bool = True, activation_token: Optional[str] = None) -> bool:
    pass


def toggle_secure_input() -> None:
    pass


def start_profiler(path: str) -> None:
    pass


def stop_profiler() -> None:
    pass


def destroy_global_data() -> None:
    pass


def current_os_window() -> Optional[int]:
    pass


def last_focused_os_window_id() -> int:
    pass


def current_focused_os_window_id() -> int:
    pass


def cocoa_set_menubar_title(title: str) -> None:
    pass


def change_os_window_state(state: str) -> None:
    pass


def change_background_opacity(os_window_id: int, opacity: float) -> bool:
    pass


def background_opacity_of(os_window_id: int) -> Optional[float]:
    pass


def read_command_response(fd: int, timeout: float, list: List[bytes]) -> None:
    pass


def wcswidth(string: str) -> int:
    pass


def is_emoji_presentation_base(code: int) -> bool:
    pass


def x11_window_id(os_window_id: int) -> int:
    pass


def cocoa_window_id(os_window_id: int) -> int:
    pass


def swap_tabs(os_window_id: int, a: int, b: int) -> None:
    pass


def set_active_tab(os_window_id: int, a: int) -> None:
    pass


def set_active_window(os_window_id: int, tab_id: int, window_id: int) -> None:
    pass


def ring_bell() -> None:
    pass


def concat_cells(cell_width: int, cell_height: int, is_32_bit: bool, cells: Tuple[bytes, ...]) -> bytes:
    pass


def current_fonts() -> Dict[str, Any]:
    pass


def remove_window(os_window_id: int, tab_id: int, window_id: int) -> None:
    pass


def remove_tab(os_window_id: int, tab_id: int) -> None:
    pass


def pt_to_px(pt: float, os_window_id: int = 0) -> int:
    pass


def next_window_id() -> int:
    pass


def mark_tab_bar_dirty(os_window_id: int) -> None:
    pass


def detach_window(os_window_id: int, tab_id: int, window_id: int) -> None:
    pass


def attach_window(os_window_id: int, tab_id: int, window_id: int) -> None:
    pass


def add_tab(os_window_id: int) -> int:
    pass


def cell_size_for_window(os_window_id: int) -> Tuple[int, int]:
    pass


def wakeup_main_loop() -> None:
    pass


class Region:
    left: int
    top: int
    right: int
    bottom: int
    width: int
    height: int

    def __init__(self, x: Tuple[int, int, int, int, int, int]):
        pass


def viewport_for_window(
    os_window_id: int
) -> Tuple[Region, Region, int, int, int, int]:
    pass


TermiosPtr = NewType('TermiosPtr', int)


def raw_tty(fd: int, termios_ptr: TermiosPtr, optional_actions: int = termios.TCSAFLUSH) -> None:
    pass


def close_tty(fd: int, termios_ptr: TermiosPtr, optional_actions: int = termios.TCSAFLUSH) -> None:
    pass


def normal_tty(fd: int, termios_ptr: TermiosPtr, optional_actions: int = termios.TCSAFLUSH) -> None:
    pass


def open_tty(read_with_timeout: bool = False, optional_actions: int = termios.TCSAFLUSH) -> Tuple[int, TermiosPtr]:
    pass


def parse_input_from_terminal(
    text_callback: Callable[[str], None], dcs_callback: Callable[[str], None],
    csi_callback: Callable[[str], None], osc_callback: Callable[[str], None],
    pm_callback: Callable[[str], None], apc_callback: Callable[[str], None],
    data: str, in_bracketed_paste: bool
) -> str:
    pass


class Line:

    def sprite_at(self, cell: int) -> Tuple[int, int, int]:
        pass


def test_shape(line: Line,
               path: Optional[str] = None,
               index: int = 0) -> List[Tuple[int, int, int, Tuple[int, ...]]]:
    pass


def test_render_line(line: Line) -> None:
    pass


def sprite_map_set_limits(w: int, h: int) -> None:
    pass


def set_send_sprite_to_gpu(
    func: Optional[Callable[[int, int, int, bytes], None]]
) -> None:
    pass


def set_font_data(
    box_drawing_func: Callable[[int, int, int, float],
                               Tuple[int, Union[bytearray, bytes, Array[c_ubyte]]]],
    prerender_func: Callable[
        [int, int, int, int, int, int, int, float, float, float, float],
        Tuple[Tuple[int, ...], Tuple[Array[c_ubyte], ...]]],
    descriptor_for_idx: Callable[[int], Tuple[FontObject, bool, bool]],
    bold: int, italic: int, bold_italic: int, num_symbol_fonts: int,
    symbol_maps: Tuple[Tuple[int, int, int], ...], font_sz_in_pts: float,
    font_feature_settings: Dict[str, Tuple[FontFeature, ...]],
    narrow_symbols: Tuple[Tuple[int, int, int], ...],
) -> None:
    pass


def get_fallback_font(text: str, bold: bool, italic: bool) -> Any:
    pass


def create_test_font_group(sz: float, dpix: float,
                           dpiy: float) -> Tuple[int, int]:
    pass


class HistoryBuf:

    def pagerhist_as_text(self, upto_output_start: bool = False) -> str:
        pass

    def pagerhist_as_bytes(self) -> bytes:
        pass


class LineBuf:

    def is_continued(self, idx: int) -> bool:
        pass

    def line(self, num: int) -> Line:
        pass


class Cursor:
    x: int
    y: int
    bg: int
    fg: int
    bold: bool
    italic: bool
    blink: bool
    shape: int


class Screen:

    color_profile: ColorProfile
    columns: int
    lines: int
    focus_tracking_enabled: bool
    historybuf: HistoryBuf
    linebuf: LineBuf
    in_bracketed_paste_mode: bool
    cursor_visible: bool
    scrolled_by: int
    cursor: Cursor
    disable_ligatures: int
    cursor_key_mode: bool
    auto_repeat_enabled: bool
    render_unfocused_cursor: int
    last_reported_cwd: Optional[str]

    def __init__(
            self,
            callbacks: Any = None,
            lines: int = 80, columns: int = 24, scrollback: int = 0,
            cell_width: int = 10, cell_height: int = 20,
            window_id: int = 0,
            test_child: Any = None
    ):
        pass

    def cursor_at_prompt(self) -> bool:
        pass

    def ignore_bells_for(self, duration: float = 1) -> None:
        pass

    def set_window_char(self, ch: str = "") -> None:
        pass

    def current_key_encoding_flags(self) -> int:
        pass

    def line(self, num: int) -> Line:
        pass

    def visual_line(self, num: int) -> Line:
        pass

    def draw(self, text: str) -> None:
        pass

    def dump_lines_with_attrs(self, acc: Callable[[str], None]) -> None:
        pass

    def apply_sgr(self, text: str) -> None:
        pass

    def copy_colors_from(self, other: 'Screen') -> None:
        pass

    def mark_as_dirty(self) -> None:
        pass

    def resize(self, width: int, height: int) -> None:
        pass

    def send_escape_code_to_child(self, code: int, text: Union[str, bytes, Tuple[Union[str, bytes], ...]]) -> bool:
        pass

    def reset_callbacks(self) -> None:
        pass

    def has_selection(self) -> bool:
        pass

    def text_for_selection(self, ansi: bool, strip_trailing_spaces: bool) -> Tuple[str, ...]:
        pass

    def is_rectangle_select(self) -> bool:
        pass

    def is_using_alternate_linebuf(self) -> bool:
        pass

    def is_main_linebuf(self) -> bool:
        pass

    def erase_in_line(self, mode: int = 0, private: bool = False) -> None:
        pass

    def scroll(self, amt: int, upwards: bool) -> bool:
        pass

    def scroll_to_next_mark(self, mark: int = 0, backwards: bool = True) -> bool:
        pass

    def scroll_to_prompt(self, num_of_prompts: int = -1) -> bool:
        pass

    def reverse_scroll(self, amt: int, fill_from_scrollback: bool = False) -> bool:
        pass

    def scroll_prompt_to_bottom(self) -> None:
        pass

    def clear_selection(self) -> None:
        pass

    def reset_mode(self, mode: int, private: bool = False) -> None:
        pass

    def refresh_sprite_positions(self) -> None:
        pass

    def set_marker(self, marker: Optional[MarkerFunc] = None) -> None:
        pass

    def paste_bytes(self, data: bytes) -> None:
        pass
    paste = paste_bytes

    def as_text(self, callback: Callable[[str], None], as_ansi: bool, insert_wrap_markers: bool) -> None:
        pass
    as_text_non_visual = as_text
    as_text_alternate = as_text
    as_text_for_history_buf = as_text

    def cmd_output(self, which: int, callback: Callable[[str], None], as_ansi: bool, insert_wrap_markers: bool) -> bool:
        pass

    def scroll_until_cursor_prompt(self) -> None:
        pass

    def reset(self) -> None:
        pass

    def erase_in_display(self, how: int = 0, private: bool = False) -> None:
        pass

    def clear_scrollback(self) -> None:
        pass

    def focus_changed(self, focused: bool) -> bool:
        pass

    def has_focus(self) -> bool:
        pass

    def has_activity_since_last_focus(self) -> bool:
        pass

    def insert_characters(self, num: int) -> None:
        pass

    def line_edge_colors(self) -> Tuple[int, int]:
        pass


def set_tab_bar_render_data(
    os_window_id: int, screen: Screen, left: int, top: int, right: int, bottom: int
) -> None:
    pass


def set_window_render_data(
    os_window_id: int, tab_id: int, window_id: int, screen: Screen,
    left: int, top: int, right: int, bottom: int
) -> None:
    pass


def truncate_point_for_length(
    text: str, num_cells: int, start_pos: int = 0
) -> int:
    pass


class ChildMonitor:

    def __init__(
        self,
        death_notify: Callable[[int], None],
        dump_callback: Optional[Callable[[bytes], None]],
        talk_fd: int = -1,
        listen_fd: int = -1,
        prewarm_fd: int = -1,
    ):
        pass

    def wakeup(self) -> None:
        pass

    def handled_signals(self) -> Tuple[int, ...]:
        pass

    def main_loop(self) -> None:
        pass

    def resize_pty(self, window_id: int, rows: int, cols: int, x_pixels: int, y_pixels: int) -> None:
        pass

    def needs_write(self, child_id: int, data: bytes) -> bool:
        pass

    def set_iutf8_winid(self, win_id: int, on: bool) -> bool:
        pass

    def add_child(self, id: int, pid: int, fd: int, screen: Screen) -> None:
        pass

    def mark_for_close(self, window_id: int) -> None:
        pass

    def start(self) -> None:
        pass

    def shutdown_monitor(self) -> None:
        pass


class KeyEvent:

    def __init__(
        self, key: int, shifted_key: int = 0, alternate_key: int = 0, mods: int = 0, action: int = 1, native_key: int = 1, ime_state: int = 0, text: str = ''
    ):
        pass

    @property
    def key(self) -> int:
        pass

    @property
    def shifted_key(self) -> int:
        pass

    @property
    def alternate_key(self) -> int:
        pass

    @property
    def mods(self) -> int:
        pass

    @property
    def action(self) -> int:
        pass

    @property
    def native_key(self) -> int:
        pass

    @property
    def ime_state(self) -> int:
        pass

    @property
    def text(self) -> str:
        pass


def set_iutf8_fd(fd: int, on: bool) -> bool:
    pass


def spawn(
    exe: str,
    cwd: str,
    argv: Tuple[str, ...],
    env: Tuple[str, ...],
    master: int,
    slave: int,
    stdin_read_fd: int,
    stdin_write_fd: int,
    ready_read_fd: int,
    ready_write_fd: int,
    handled_signals: Tuple[int, ...],
    kitten_exe: str,
) -> int:
    pass


def set_window_padding(os_window_id: int, tab_id: int, window_id: int, left: int, top: int, right: int, bottom: int) -> None:
    pass


def click_mouse_url(os_window_id: int, tab_id: int, window_id: int) -> bool:
    pass


def click_mouse_cmd_output(os_window_id: int, tab_id: int, window_id: int, select_cmd_output: bool) -> bool:
    pass


def move_cursor_to_mouse_if_in_prompt(os_window_id: int, tab_id: int, window_id: int) -> bool:
    pass


def mouse_selection(os_window_id: int, tab_id: int, window_id: int, code: int, button: int) -> None:
    pass


def set_window_logo(os_window_id: int, tab_id: int, window_id: int, path: str, position: str, alpha: float) -> None:
    pass


def apply_options_update() -> None:
    pass


def set_os_window_size(os_window_id: int, x: int, y: int) -> bool:
    pass


class OSWindowSize(TypedDict):
    width: int
    height: int
    framebuffer_width: int
    framebuffer_height: int
    xscale: float
    yscale: float
    xdpi: float
    ydpi: float
    cell_width: int
    cell_height: int


def mark_os_window_dirty(os_window_id: int) -> None:
    pass


def get_os_window_size(os_window_id: int) -> Optional[OSWindowSize]:
    pass


def get_all_processes() -> Tuple[int, ...]:
    pass


def num_users() -> int:
    pass


def redirect_mouse_handling(yes: bool) -> None:
    pass


def get_click_interval() -> float:
    pass


def send_data_to_peer(peer_id: int, data: Union[str, bytes]) -> None:
    pass


def set_os_window_title(os_window_id: int, title: str) -> None:
    pass


def get_os_window_title(os_window_id: int) -> Optional[str]:
    pass


def update_ime_position_for_window(window_id: int, force: bool = False, update_focus: int = 0) -> bool:
    pass


def shm_open(name: str, flags: int, mode: int = 0o600) -> int:
    pass


def shm_unlink(name: str) -> None:
    pass


def sigqueue(pid: int, signal: int, value: int) -> None:
    pass


def random_unix_socket() -> int:
    pass


def read_signals(fd: int, callback: Callable[[SignalInfo], None]) -> None:
    pass


def install_signal_handlers(*signals: int) -> Tuple[int, int]:
    pass


def remove_signal_handlers() -> None:
    pass


def getpeereid(fd: int) -> Tuple[int, int]:
    pass


X25519: int
SHA1_HASH: int
SHA224_HASH: int
SHA256_HASH: int
SHA384_HASH: int
SHA512_HASH: int


class Secret:
    pass


class EllipticCurveKey:

    def __init__(
        self, algorithm: int = 0  # X25519
    ): pass

    def derive_secret(
        self, pubkey: bytes, hash_algorithm: int = 0  # SHA256_HASH
    ) -> Secret: pass

    @property
    def public(self) -> bytes: ...

    @property
    def private(self) -> Secret: ...


class AES256GCMEncrypt:

    def __init__(self, key: Secret): ...

    def add_authenticated_but_unencrypted_data(self, data: bytes) -> None: ...

    def add_data_to_be_encrypted(self, data: bytes, finished: bool = False) -> bytes: ...

    @property
    def iv(self) -> bytes: ...

    @property
    def tag(self) -> bytes: ...


class AES256GCMDecrypt:

    def __init__(self, key: Secret, iv: bytes, tag: bytes): ...

    def add_data_to_be_authenticated_but_not_decrypted(self, data: bytes) -> None: ...

    def add_data_to_be_decrypted(self, data: bytes, finished: bool = False) -> bytes: ...


class SingleKey:

    __slots__ = ()

    def __init__(self, mods: int = 0, is_native: object = False, key: int = -1): ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __getitem__(self, x: int) -> int: ...
    @property
    def mods(self) -> int: ...
    @property
    def is_native(self) -> bool: ...
    @property
    def key(self) -> int: ...
    @property
    def defined_with_kitty_mod(self) -> bool: ...
    def __iter__(self) -> Iterator[int]: ...
    def _replace(self, mods: int = 0, is_native: object = False, key: int = -1) -> 'SingleKey': ...
    def resolve_kitty_mod(self, mod: int) -> 'SingleKey': ...


def set_use_os_log(yes: bool) -> None: ...
def get_docs_ref_map() -> bytes: ...
def clearenv() -> None: ...
def set_clipboard_data_types(ct: int, mime_types: Tuple[str, ...]) -> None: ...
def get_clipboard_mime(ct: int, mime: Optional[str], callback: Callable[[bytes], None]) -> None: ...
def run_with_activation_token(func: Callable[[str], None]) -> None: ...
def make_x11_window_a_dock_window(x11_window_id: int, strut: Tuple[int, int, int, int, int, int, int, int, int, int, int, int]) -> None: ...
def unicode_database_version() -> Tuple[int, int, int]: ...
def wrapped_kitten_names() -> List[str]: ...
def expand_ansi_c_escapes(test: str) -> str: ...
def update_tab_bar_edge_colors(os_window_id: int) -> bool: ...
def mask_kitty_signals_process_wide() -> None: ...
def is_modifier_key(key: int) -> bool: ...
