#!/usr/bin/env python3

import argparse

from slapdash.app import app


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", metavar="PORT", default=8050, type=int)
    parser.add_argument("--host", metavar="HOST", default='localhost')
    parser.add_argument('--debug', action='store_true', default=True)
    parser.add_argument("--processes", metavar="PROCESSES", type=int, default=1)
    parser.add_argument("--threaded", action='store_true')
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
