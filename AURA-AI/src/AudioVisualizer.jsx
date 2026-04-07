import React from 'react';

export const AudioVisualizer = ({ isSpeaking, volumeLevel }) => {
    const bars = Array.from({ length: 30 }, (_, i) => i);
    const baseHeight = 2;
    const maxHeight = 25;

    return (
        <div className="flex justify-center items-center h-16 w-full max-w-sm">
            {bars.map((index) => {
                let height;
                if (isSpeaking) {
                    const sine = Math.sin(index * 0.4 + Date.now() * 0.005);
                    height = 10 + sine * 5;
                } else {
                    const normalizedVolume = Math.min(volumeLevel * 150, 1);
                    const distanceFromCenter = Math.abs(index - bars.length / 2);
                    const barVolume = Math.max(0, normalizedVolume - distanceFromCenter * 0.04);
                    height = baseHeight + barVolume * (maxHeight - baseHeight);
                }
                
                return (
                    <div
                        key={index}
                        className="w-1 rounded-full bg-cyan-300/40"
                        style={{ height: `${Math.max(baseHeight, height)}px`, margin: '0 2px', transition: 'height 0.1s ease-out' }}
                    ></div>
                );
            })}
        </div>
    );
};