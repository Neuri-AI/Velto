"""Declarative UI, hooks, rendering, and extension APIs supplied by PSX."""

from psx import (
    App,
    Badge,
    Button,
    Checkbox,
    ComponentAdapter,
    ComponentDefinition,
    ComponentRegistry,
    Divider,
    DuplicateKeyError,
    Flex,
    Fragment,
    Grid,
    GridItem,
    HookOrderError,
    Image,
    Input,
    InvalidChildError,
    Link,
    MarkupSyntaxError,
    Native,
    NativeOwnership,
    NativeWidget,
    PLUGIN_ENTRY_POINT_GROUP,
    PSXError,
    Plugin,
    PluginAPI,
    ProgressBar,
    Radio,
    RadioGroup,
    Ref,
    RendererAdapterRegistry,
    RendererCapabilities,
    RendererCapabilityError,
    RendererConfigurationError,
    Scroll,
    Select,
    Slider,
    Spacer,
    SpinBox,
    Switch,
    Text,
    TextArea,
    ThreadViolationError,
    VNode,
    WebView,
    builtin_component_registry,
    component,
    create_element,
    load_plugins,
    native_widget,
    native_adapter,
    psx,
    register_adapter,
    register_component,
    renderer_capabilities,
    use_effect,
    use_ref,
    use_state,
)
# Pydux is an optional state integration; PSX UI must work without it.
try:
    from pydux import MainThreadBridge, Reactive, ReactiveBinding, connect, connect_qyro
except ImportError as error:
    if not (error.name == "pydux" or (error.name or "").startswith("pydux.")):
        raise
    # The Pydux-specific names are deliberately not exposed when absent.
    pass

__all__ = [
    "App", "Badge", "Button", "Checkbox", "ComponentAdapter", "ComponentDefinition",
    "ComponentRegistry", "Divider", "DuplicateKeyError", "Flex", "Fragment", "Grid",
    "GridItem", "HookOrderError", "Image", "Input", "InvalidChildError", "Link",
    "MainThreadBridge", "MarkupSyntaxError", "Native", "NativeOwnership", "NativeWidget",
    "PLUGIN_ENTRY_POINT_GROUP", "PSXError", "Plugin", "PluginAPI", "ProgressBar",
    "Radio", "RadioGroup", "Reactive",
    "ReactiveBinding", "Ref", "RendererAdapterRegistry", "RendererCapabilities",
    "RendererCapabilityError", "RendererConfigurationError", "Scroll", "Select", "Slider",
    "Spacer", "SpinBox", "Switch", "Text", "TextArea", "WebView",
    "ThreadViolationError", "VNode", "builtin_component_registry", "component", "connect",
    "connect_qyro", "create_element", "load_plugins", "native_widget", "native_adapter", "psx",
    "register_adapter", "register_component", "renderer_capabilities", "use_effect", "use_ref",
    "use_state",
]

# Only publish Pydux integration symbols if the optional dependency is installed.
_PYDUX_NAMES = ("MainThreadBridge", "Reactive", "ReactiveBinding", "connect", "connect_qyro")
__all__ = [name for name in __all__ if name not in _PYDUX_NAMES or name in globals()]
