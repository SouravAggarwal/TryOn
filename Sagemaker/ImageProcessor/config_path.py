CKPT_PATH = None
OPENPOSE_INNER_CKPT_PATH = None
CREATE_CACHE = 1


def process_command_line_args(parser):
    global CKPT_PATH, OPENPOSE_INNER_CKPT_PATH, CREATE_CACHE  # Use global to modify module-level variables
    parser.add_argument('--ckpt', type=str, help='ckpt folder path')
    parser.add_argument('--create_cache', type=int, help='Create a cache directory for models to download')

    args = parser.parse_args()
    CKPT_PATH = args.ckpt if args.ckpt else "ckpt"
    OPENPOSE_INNER_CKPT_PATH = f'{CKPT_PATH}/openpose/ckpts'
    CREATE_CACHE = args.create_cache

    print(f"-gradio_demo.config_path.process_command_line_args(): CKPT_PATHs: {CKPT_PATH} and {OPENPOSE_INNER_CKPT_PATH}")
    print('create_cache:', CREATE_CACHE)

