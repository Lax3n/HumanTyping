import numpy as np
from .typer import MarkovTyper
import time
import sys

def run_monte_carlo(target_text, wpm, n_simulations=100):
    """
    Runs n_simulations to estimate typing time distribution.
    """
    times = []
    print(f"Running {n_simulations} simulations for text: '{target_text}' (Target WPM: {wpm})")
    
    start_global = time.time()
    
    for i in range(n_simulations):
        typer = MarkovTyper(target_text, target_wpm=wpm)
        total_time, _ = typer.run()
        times.append(total_time)
        
    end_global = time.time()
    
    times = np.array(times)
    mean_time = np.mean(times)
    std_time = np.std(times)
    min_time = np.min(times)
    max_time = np.max(times)
    
    print(f"\n--- Monte Carlo Results ---")
    print(f"Estimated Mean Time : {mean_time:.4f} s")
    print(f"Standard Deviation  : {std_time:.4f} s")
    print(f"Min / Max           : {min_time:.4f} s / {max_time:.4f} s")
    print(f"Computation Time    : {end_global - start_global:.4f} s")
    
    return times

def demo_single_run(target_text, wpm):
    """
    Displays a detailed real-time simulation.
    """
    print(f"\n--- Real-Time Simulation Demo: '{target_text}' (Target WPM: {wpm}) ---")
    print("Preparing simulation...\n")
    
    # 1. Calculate trajectory instantly
    typer = MarkovTyper(target_text, target_wpm=wpm)
    total_time, history = typer.run()
    
    # 2. Replay history
    print("START TYPING:")
    print("-" * 40)
    
    last_time = 0.0
    
    for t, action, text in history:
        # Calculate delay
        delay = t - last_time
        if delay > 0:
            time.sleep(delay)
            
        last_time = t
        
        # Visual feedback
        # If action is arrow key, we show it
        indicator = ""
        if "ARROW" in action:
            indicator = f"   <-- {action}"
        elif "BACKSPACE" in action:
            indicator = "   <-- BACKSPACE"
            
        # Clear line and rewrite
        # \r return chariot, \033[K efface la fin de ligne
        sys.stdout.write(f"\r{text}{indicator}")
        sys.stdout.flush()
        
    print(f"\r{target_text}                                      ") 
    print("-" * 40)
    print(f"\nTotal Simulated Time: {total_time:.4f}s")
    
    # Show errors
    errors = [h for h in history if "ERROR" in h[1]]
    if errors:
        print(f"\nErrors made and corrected: {len(errors)}")
