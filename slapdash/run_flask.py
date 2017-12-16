import argparse

from .app import app


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", metavar="PORT", default=8052, type=int)
    parser.add_argument("--host", metavar="HOST", default='0.0.0.0')
    parser.add_argument("--processes", metavar="PROCESSES", type=int, default=1)
    parser.add_argument("--threaded", action='store_true')

    # default debug to on, but have option to turn off
    debug_parser = parser.add_mutually_exclusive_group(required=False)
    debug_parser.add_argument('--debug', dest='debug', action='store_true')
    debug_parser.add_argument('--no-debug', dest='debug', action='store_false')
    parser.set_defaults(debug=True)
    return parser



def main():
    args = argparser().parse_args()
    app.server.run(
        debug=args.debug,
        host=args.host,
        port=args.port,
        processes=args.processes,
        threaded=args.threaded,
    )


if __name__ == '__main__':
    main()
