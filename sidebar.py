import streamlit as st # type: ignore
from config import MODEL_OPTIONS, KNOWN_OBJECT_SIZES, DEFAULT_CONFIDENCE, DEFAULT_DISTANCE_THRESHOLD, DEFAULT_FOCAL_LENGTH

def render_sidebar():
    """Render and return all sidebar settings"""
    with st.sidebar:
        st.markdown("### 🎛️ Control Panel")
        
        # Model selection
        st.markdown("#### 🤖 AI Model")
        model_option = st.selectbox(
            "Select Detection Model",
            list(MODEL_OPTIONS.keys()),
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Camera settings
        st.markdown("#### 📹 Camera Settings")
        camera_index = st.selectbox("Camera Source", [0, 1, 2], help="Select camera input")
        confidence = st.slider("Detection Confidence", 0.0, 1.0, DEFAULT_CONFIDENCE, 0.05)
        
        st.markdown("---")
        
        # Alarm settings
        st.markdown("#### 🚨 Proximity Alert System")
        enable_alarm = st.toggle("Enable Alarm", value=True)
        
        if enable_alarm:
            distance_threshold = st.slider(
                "Alert Distance (meters)",
                1.0, 20.0, DEFAULT_DISTANCE_THRESHOLD, 0.5,
                help="Trigger alarm when objects are closer than this distance"
            )
            alarm_type = st.selectbox("Alarm Type", ["Beep", "Siren", "Voice Alert"])
        else:
            distance_threshold = DEFAULT_DISTANCE_THRESHOLD
            alarm_type = "Beep"
        
        st.markdown("---")
        
        # Calibration
        st.markdown("#### 📏 Distance Calibration")
        focal_length = st.number_input(
            "Focal Length (pixels)",
            100, 2000, DEFAULT_FOCAL_LENGTH, 50,
            help="Adjust for accurate distance measurement"
        )
        
        st.markdown("---")
        
        # Object monitoring
        st.markdown("#### 🎯 Object Monitoring")
        monitor_all = st.toggle("Monitor All Objects", value=True)
        
        if not monitor_all:
            monitored_objects = st.multiselect(
                "Select Objects",
                list(KNOWN_OBJECT_SIZES.keys()),
                default=["person", "car"],
                label_visibility="collapsed"
            )
        else:
            monitored_objects = list(KNOWN_OBJECT_SIZES.keys())
        
        st.markdown("---")
        
        # Display options
        st.markdown("#### 📺 Display Options")
        col1, col2 = st.columns(2)
        with col1:
            show_distance = st.checkbox("Distance", value=True)
            show_labels = st.checkbox("Labels", value=True)
        with col2:
            show_conf = st.checkbox("Confidence", value=True)
            show_fps = st.checkbox("FPS", value=True)
    
    return {
        'model_option': model_option,
        'camera_index': camera_index,
        'confidence': confidence,
        'enable_alarm': enable_alarm,
        'distance_threshold': distance_threshold,
        'alarm_type': alarm_type,
        'focal_length': focal_length,
        'monitored_objects': monitored_objects,
        'show_distance': show_distance,
        'show_labels': show_labels,
        'show_conf': show_conf,
        'show_fps': show_fps
    }
