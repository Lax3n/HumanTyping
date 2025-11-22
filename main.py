import argparse
import sys
from humantyping.simulation import run_monte_carlo, demo_single_run

def main():
    parser = argparse.ArgumentParser(description="Keyboard Typing Simulation via Markov Chains")
    parser.add_argument("text", nargs="?", default="Hello world", help="The text to simulate")
    parser.add_argument("--mode", choices=["demo", "montecarlo"], default="demo", help="Execution mode")
    parser.add_argument("--n", type=int, default=100, help="Number of simulations for Monte Carlo")
    parser.add_argument("--wpm", type=float, default=60.0, help="Target average speed (Words Per Minute)")
    
    args = parser.parse_args()
    
    if args.mode == "demo":
        demo_single_run(args.text, args.wpm)
    elif args.mode == "montecarlo":
        run_monte_carlo(args.text, args.wpm, n_simulations=args.n)

if __name__ == "__main__":
    main()
